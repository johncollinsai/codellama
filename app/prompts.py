# gpt-4
USER_PROMPT = """
Please describe this code {prompt}. 
Please check and comment upon the following where appropriate to do so, with regard to {prompt}:
- The code's correctness
- The code's style
- The code's efficiency
- The code's readability
- The code's maintainability
- The code's security
- The code's robustness
- The code's scalability
- The code's testability
If possible recommend improvements to {prompt}:
"""

# codellama-7b
USER_PROMPT_LLAMA = """
Please describe this code {prompt}. 
"""