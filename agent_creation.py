from my_conversable_agent import MyConversableAgent
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from config import config_list
from search_functions import google_search
from web_scraping_functions import web_scraping

def create_user_proxy(chat_interface):
    user_proxy = MyConversableAgent(
        chat_interface=chat_interface,
        name="Admin",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        system_message="""A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.  
        """,
        code_execution_config=False,
        human_input_mode="ALWAYS",
    )
    return user_proxy

def create_researcher():
    researcher = GPTAssistantAgent(
        name = "researcher",
        llm_config = {
            "config_list": config_list,
            "assistant_id": "asst_aPJMdifV02oopBypJPxYgAKw"
        }
    )
    researcher.register_function(
        function_map={
            "google_search": google_search,
            "web_scraping": web_scraping
        }
    )
    return researcher

def create_research_manager():
    research_manager = GPTAssistantAgent(
        name="research_manager",
        llm_config = {
            "config_list": config_list,
            "assistant_id": "asst_vzMkR7T4kiwwxbJ4wF7cE3XJ"
        }
    )
    return research_manager