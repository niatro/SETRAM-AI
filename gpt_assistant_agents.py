from autogen import config_list_from_json
from my_conversable_agent import MyConversableAgent
from search_functions import google_search
from web_scraping_functions import web_scraping

config_list = config_list_from_json("OAI_CONFIG_LIST")

class GPTAssistantAgent(MyConversableAgent):
    def __init__(self, chat_interface, *args, **kwargs):
        super().__init__(chat_interface, *args, **kwargs)
        # Aquí puedes agregar cualquier inicialización adicional que necesites para GPTAssistantAgent

    # Aquí puedes agregar cualquier método adicional que necesites para GPTAssistantAgent

def create_agents(chat_interface):
    user_proxy = MyConversableAgent(
        chat_interface,
        name="Admin",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        system_message="""A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.""",
        code_execution_config=False,
        human_input_mode="ALWAYS",
    )

    research_manager = GPTAssistantAgent(
        chat_interface,
        name="research_manager",
        llm_config = {
            "config_list": config_list,
            "assistant_id": "asst_vzMkR7T4kiwwxbJ4wF7cE3XJ"
        }
    )

    researcher = GPTAssistantAgent(
        chat_interface,
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

    return user_proxy, research_manager, researcher