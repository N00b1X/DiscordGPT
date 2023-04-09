import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT')
API_KEY = os.getenv('OPENAI_API_KEY_PAWAN')


def chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY
    }
    request_data = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 50,
        'temperature': 0.5
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=request_data)
    if response.status_code != 200:
        print(f'Request failed with status code: {response.status_code}')
    else:
        prompt_response = response.json()['choices'][0]['text']
    return prompt_response
