import asyncio
import autogen

input_future = None  # Assuming this is a global variable used in your code

class MyConversableAgent(autogen.ConversableAgent):
    def __init__(self, chat_interface, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chat_interface = chat_interface

    def initialize(self, chat_interface):
        self.chat_interface = chat_interface

    async def a_get_human_input(self, prompt: str) -> str:
        global input_future
        print('AGET!!!!!!')  # or however you wish to display the prompt
        self.chat_interface.send(prompt, user="System", respond=False)
        # Create a new Future object for this input operation if none exists
        if input_future is None or input_future.done():
            input_future = asyncio.Future()

        # Wait for the callback to set a result on the future
        await input_future

        # Once the result is set, extract the value and reset the future for the next input operation
        input_value = input_future.result()
        input_future = None
        return input_value