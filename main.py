import autogen
import panel as pn 
from chat_functions import callback
from config import gpt4_config
from agent_creation import create_user_proxy, create_researcher, create_research_manager
from write_content import write_content


def initialize_chat():
    chat_interface = pn.chat.ChatInterface(callback=lambda contents, user, instance: callback(contents, user, instance, user_proxy, manager))

    # Crear user_proxy
    user_proxy = create_user_proxy(chat_interface)

    # Crear researcher
    researcher = create_researcher()

    # Crear research_manager
    research_manager = create_research_manager()

    groupchat = autogen.GroupChat(agents=[user_proxy,  researcher, research_manager], messages=[], max_round=20)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

    avatar = {user_proxy.name:"👨‍💼", research_manager.name:"👩‍💻", researcher.name:"🛠"}

    agents = [user_proxy, researcher, research_manager]
    for agent in agents:
        agent.register_reply(
            [autogen.Agent, None],
            reply_func=print_messages, 
            config={"callback": None},
        )

    return chat_interface, avatar

def print_messages(recipient, messages, sender, config):
    last_message = messages[-1]
    sender_name = last_message.get('name', 'SecretGuy')
    avatar_icon = avatar.get(sender_name, '🥷')
    content = last_message['content']

    print(f"Messages from: {sender.name} sent to: {recipient.name} | num messages: {len(messages)} | message: {last_message}")
    chat_interface.send(content, user=sender_name, avatar=avatar_icon, respond=False)

     # Después de que se haya completado el chat inicial, llama a la función write_content
    if sender.name == "research_manager" and recipient.name == "user_proxy":
        research_material = "Aquí va el material de investigación"  # Reemplaza esto con el material de investigación real
        topic = "Aquí va el tema"  # Reemplaza esto con el tema real
        write_content(chat_interface, research_material, topic)
    
    return False, None  # required to ensure the agent communication flow continues

def send_initial_message(chat_interface):
    chat_interface.send("Enviar un mensaje!", user="System", respond=False)

pn.extension(design="material")

chat_interface, avatar = initialize_chat()
send_initial_message(chat_interface)
chat_interface.servable()


  
