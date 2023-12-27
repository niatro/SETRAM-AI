# search_functions.py
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
serper_api_key = os.getenv("SERP_API_KEY")

def google_search(search_keyword):    
    url = "https://google.serper.dev/search"
    
    payload = json.dumps({
        "q": search_keyword
    })

    headers = {
        'X-API-KEY': serper_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

