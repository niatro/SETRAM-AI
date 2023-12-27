import os
import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from bs4 import BeautifulSoup
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import json
from autogen import config_list_from_json
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent
import autogen
import panel as pn 
import asyncio
from search_functions import google_search
from web_scraping_functions import web_scraping
from summary_functions import resumen
from my_conversable_agent import MyConversableAgent
from chat_functions import delayed_initiate_chat, callback



load_dotenv()
brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")
serper_api_key = os.getenv("SERP_API_KEY")
airtable_api_key = os.getenv("AIRTABLE_API_KEY")
config_list = config_list_from_json("OAI_CONFIG_LIST")
gpt4_config = {"config_list": config_list, "temperature":0, "seed": 53} # El seed hace deterministica la respuesta




chat_interface = pn.chat.ChatInterface(callback=lambda contents, user, instance: callback(contents, user, instance, user_proxy, manager))

user_proxy = MyConversableAgent(
    chat_interface=chat_interface,
    name="Admin",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    system_message="""A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.  
    """,
    code_execution_config=False,
    human_input_mode="ALWAYS",
)

# Crear agente investigador
researcher = GPTAssistantAgent(
    name = "researcher",
    llm_config = {
        "config_list": config_list,
        "assistant_id": "asst_aPJMdifV02oopBypJPxYgAKw"
    }
)
# Crear las funciones que usara el researcher
researcher.register_function(
        function_map={
            "google_search": google_search,
            "web_scraping": web_scraping
            
        }
    )

# Crear agente administrador de investigación
research_manager = GPTAssistantAgent(
    name="research_manager",
    llm_config = {
        "config_list": config_list,
        "assistant_id": "asst_vzMkR7T4kiwwxbJ4wF7cE3XJ"
    }
)



groupchat = autogen.GroupChat(agents=[user_proxy,  researcher, research_manager], messages=[], max_round=20)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

avatar = {user_proxy.name:"👨‍💼", research_manager.name:"👩‍💻", researcher.name:"🛠"}

def print_messages(recipient, messages, sender, config):

    #chat_interface.send(messages[-1]['content'], user=messages[-1]['name'], avatar=avatar[messages[-1]['name']], respond=False)
    print(f"Messages from: {sender.name} sent to: {recipient.name} | num messages: {len(messages)} | message: {messages[-1]}")
    
    if all(key in messages[-1] for key in ['name']):
        chat_interface.send(messages[-1]['content'], user=messages[-1]['name'], avatar=avatar[messages[-1]['name']], respond=False)
    else:
        chat_interface.send(messages[-1]['content'], user='SecretGuy', avatar='🥷', respond=False)
    
    return False, None  # required to ensure the agent communication flow continues

user_proxy.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
)

researcher.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
) 

research_manager.register_reply(
    [autogen.Agent, None],
    reply_func=print_messages, 
    config={"callback": None},
) 


pn.extension(design="material")
initiate_chat_task_created = False



chat_interface.send("Enviar un mensaje!", user="System", respond=False)
chat_interface.servable()
  
