# web_scraping_functions.py
import requests
import json
from bs4 import BeautifulSoup
from summary_functions import resumen

def web_scraping(objective: str, url: str, browserless_api_key):
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
    }

    data = {
        "url": url        
    }

    data_json = json.dumps(data)
    response = requests.post(f"https://chrome.browserless.io/content?token={browserless_api_key}", headers=headers, data=data_json)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        if len(text) > 10000:
            output = resumen(objective,text)
            return output
        else:
            return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")   