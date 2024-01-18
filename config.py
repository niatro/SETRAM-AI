import os
from dotenv import load_dotenv
from autogen import config_list_from_json

# Cargar variables de entorno
load_dotenv()
brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")
serper_api_key = os.getenv("SERP_API_KEY")
airtable_api_key = os.getenv("AIRTABLE_API_KEY")
open_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Cargar lista de configuración
config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt4-1106-preview"]
                 }
)

# Configuración de gpt4
gpt4_config = {"config_list": config_list, "temperature":0, "seed": 53} # El seed hace deterministica la respuesta