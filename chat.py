import panel as pn

def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    message = f"Echoing {user:} {contents}"
    return message


chat_interface=pn.chat.ChatInterface(callback=callback)

chat_interface.send(
    "Fnter a message in the Text Input below and receive an echo!",
    user="System",
    respond=False,
)
chat_interface.servable()