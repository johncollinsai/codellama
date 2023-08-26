import requests
import traceback
import os
import re
import openai
import fire
import torch
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
from .validatename import validate_company_name_gpt
from .prompts import INTRO_SENTENCE, USER_PROMPT, USER_PROMPT_LLAMA
from llama import Llama

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    
    return api_key

api_key = get_api_key()

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'

    # initialize the process group
    torch.distributed.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    torch.distributed.destroy_process_group()

def generate_gpt4_response(
        prompt, 
        modality, 
        api_key, 
        ckpt_dir, 
        tokenizer_path, 
        max_seq_len=100, # max length of the input sequence, set to 25 because llama-2-7b seems to work in simple Q&A fashion
        max_gen_len=1500, # max length of the generated sequence, set to 1500 as kind of comparable to 1500 for gpt-4 max_tokens
        max_batch_size=4, 
        temperature=0, # 0 implies models will always pick the most likely next word, ignoring top_p re llama-2, aligns with gpt-4
        top_p=0.9 # overridden here by temperature=0, aligns with gpt-4
    ):
    try:
        print("Prompt: ", prompt)   # print prompt
        print("Modality: ", modality)   # print api key

        is_valid = validate_company_name_gpt(prompt, modality, api_key)
        
        if not is_valid:
            raise ValueError(f"Invalid company name: {prompt}")
        
        intro_sentence = INTRO_SENTENCE.format(modality=modality, prompt=prompt)
        user_prompt = USER_PROMPT.format(modality=modality, prompt=prompt, intro_sentence=intro_sentence)
        user_prompt_llama = USER_PROMPT_LLAMA.format(prompt=prompt)
        
        openai.api_key = api_key

        if modality == "gpt-4":
            def create_chat_completion():
                return openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"You are an AI trained to provide detailed and accurate {modality} information about companies."},
                        {"role": "user", "content": user_prompt}
                    ],
                    max_tokens=1500,
                    n=1,
                    stop=None,
                    temperature=0,
                )

            # Create the chat completion
            response = create_chat_completion()

            print(modality, " response:", response)  # print statements to see the values of variables and the response from the GPT-4 API

            final_response = response['choices'][0]['message']['content']
            return final_response.strip()
        
        elif modality == "llama-2-7b":
            setup(0, 1)  # initialize the process group with rank=0, world_size=1
            generator = Llama.build(
                ckpt_dir=ckpt_dir,
                tokenizer_path=tokenizer_path,
                max_seq_len=max_seq_len,
                max_batch_size=max_batch_size,
            )
            prompts = [user_prompt_llama]
            try:
                results = generator.text_completion(
                    prompts,
                    max_gen_len=max_gen_len,
                    temperature=temperature,
                    top_p=top_p,
                )
                for result in results:
                    print(f"{modality} response:")
                    print(f"> {result['generation']}")
                return results[0]['generation'].strip()

            except Exception as e:
                print(f"An error of type {type(e).__name__} occurred during the generation: {str(e)}")
                traceback.print_exc()
                return str(e)

            finally:
                cleanup()  # cleanup the process group

    # part of try/except block, here the except block catches error and prints it to the terminal
    except Exception as e:
        print(f"An error of type {type(e).__name__} occurred during the generation: {str(e)}")
        traceback.print_exc()
        return str(e)
