import os

import requests
from dotenv import load_dotenv

load_dotenv()

# use your API_ENDPOINT and your API_KEY
API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT')
API_KEY = os.getenv('OPENAI_API_KEY_PAWAN')


def chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY
    }
    request_data = {
        # type of model to use for the response
        'model': 'text-davinci-003',
        'prompt': prompt,
        # length of the response you get
        'max_tokens': 50,
        # creativity of the response
        'temperature': 0.5
    }
    # make a POST request to the API_ENDPOINT and save it to variable
    response = requests.post(API_ENDPOINT, headers=headers, json=request_data)
    # checking for valid response
    if response.status_code != 200:
        print(f'Request failed with status code: {response.status_code}')
    else:
        # the response is in json format, se we take only a part of it do display
        prompt_response = response.json()['choices'][0]['text']
    return prompt_response
