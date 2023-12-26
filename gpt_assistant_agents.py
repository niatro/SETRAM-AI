# gpt_assistant_agent.py
from my_conversable_agent import MyConversableAgent

class GPTAssistantAgent(MyConversableAgent):
    def __init__(self, chat_interface, *args, **kwargs):
        super().__init__(chat_interface, *args, **kwargs)
        # Aquí puedes agregar cualquier inicialización adicional que necesites para GPTAssistantAgent

    # Aquí puedes agregar cualquier método adicional que necesites para GPTAssistantAgent
        

from my_conversable_agent import MyConversableAgent
from gpt_assistant_agents import GPTAssistantAgent
from search_functions import google_search
from web_scraping_functions import web_scraping

# Define user_proxy
user_proxy = MyConversableAgent(
   name="Admin",
   is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
   system_message="""A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.  
   """,
   code_execution_config=False,
   human_input_mode="ALWAYS",
)

# Define manager (research_manager in your original code)
config_list = ...  # Define config_list
research_manager = GPTAssistantAgent(
    name="research_manager",
    llm_config = {
        "config_list": config_list,
        "assistant_id": "asst_vzMkR7T4kiwwxbJ4wF7cE3XJ"
    }
)

# Define researcher and register its functions
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