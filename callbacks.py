import asyncio
import panel as pn
from chat_functions import delayed_initiate_chat

async def callback(user_proxy, manager, contents: str, user: str, instance: pn.chat.ChatInterface):
    global initiate_chat_task_created
    global input_future

    if not initiate_chat_task_created:
        asyncio.create_task(delayed_initiate_chat(user_proxy, manager, contents))
    else:
        if input_future and not input_future.done():
            input_future.set_result(contents)
        else:
            print("Actualmente no hay ninguna respuesta en espera.")