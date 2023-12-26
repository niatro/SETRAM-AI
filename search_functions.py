# search_functions.py
import requests
import json

def google_search(search_keyword, serper_api_key):    
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

