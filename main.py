import os
import asyncio
import panel as pn
from search_functions import google_search
from web_scraping_functions import web_scraping
from my_conversable_agent import MyConversableAgent
from callbacks import callback
from autogen import config_list_from_json
from gpt_assistant_agents import user_proxy, research_manager, researcher
import autogen


# Load API keys from environment variables
serper_api_key = os.getenv("SERP_API_KEY")
browserless_api_key = os.getenv("BROWSERLESS_API_KEY")
config_list = config_list_from_json("OAI_CONFIG_LIST")
gpt4_config = {"config_list": config_list, "temperature":0, "seed": 53} # El seed hace deterministica la respuesta

# Create chat interface
chat_interface = pn.chat.ChatInterface(callback=callback)
my_agent = MyConversableAgent(chat_interface)

groupchat = autogen.GroupChat(agents=[user_proxy, researcher, research_manager], messages=[], max_round=20)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)



# ... rest of your code ...
chat_interface = pn.chat.ChatInterface(callback=callback)
chat_interface.send("Enviar un mensaje!", user="System", respond=False)
chat_interface.servable()
  