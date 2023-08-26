import random
import asyncio
import requests  

from flask import Blueprint, render_template, request, jsonify
from .completions import generate_gpt4_response, get_api_key

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@bp.route('/get_completion', methods=["POST"])
def get_completion():
    try:
        prompt = request.form['prompt']
        modality = request.form['modality']
        api_key = get_api_key()

        # You should replace the strings 'path_to_checkpoint' and 'path_to_tokenizer' with the actual paths
        ckpt_dir = '/home/john/llama/llama-2-7b'
        tokenizer_path = '/home/john/llama/tokenizer.model'

        # Generate response for the given modality
        response = generate_gpt4_response(prompt, modality, api_key, ckpt_dir, tokenizer_path)
        
        return jsonify({"success": True, "response": response})
    
    except ValueError as e:
        # jsonify() converts Python dictionary to JSON for the specific modality
        return jsonify({"success": False, "error": str(e)})


