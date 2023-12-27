# web_scraping_functions.py
import os
import requests
import json
from bs4 import BeautifulSoup
from summary_functions import resumen
from dotenv import load_dotenv


load_dotenv()
brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")

def web_scraping(objective: str, url: str):
    #scrape sitio web, y también resumirá el contenido según el objetivo si el contenido es demasiado grande
    #objetivo es el objetivo y la tarea originales que el usuario le asigna al agente, la URL es la URL del sitio web que se va a eliminar.

    print("Scraping website...")
    # Define the headers for the request
    headers = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json',
    }

    # Define the data to be sent in the request
    data = {
        "url": url        
    }

    # Convert Python object to JSON string
    data_json = json.dumps(data)

    # Send the POST request
    response = requests.post(f"https://chrome.browserless.io/content?token={brwoserless_api_key}", headers=headers, data=data_json)
    
    # Check the response status code
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        print("CONTENTTTTTT:", text)
        if len(text) > 10000:
            output = resumen(objective,text)
            return output
        else:
            return text
    else:
        print(f"HTTP request failed with status code {response.status_code}")  