import asynctest
from unittest.mock import AsyncMock, patch
from my_conversable_agent import MyConversableAgent

class TestMyConversableAgent(asynctest.TestCase):
    def setUp(self):
        self.chat_interface = AsyncMock()
        self.agent = MyConversableAgent(self.chat_interface, 'Test Agent')

    @patch('my_conversable_agent.MyConversableAgent.a_get_human_input', new_callable=AsyncMock)
    async def test_a_get_human_input(self, mock_a_get_human_input):
        # Arrange
        async def side_effect(prompt):
            self.chat_interface.send(prompt, user="System", respond=False)
            return "test input"
        mock_a_get_human_input.side_effect = side_effect
        prompt = "Test prompt"

        # Act
        result = await self.agent.a_get_human_input(prompt)

        # Print out the result for debugging
        print(result)

        # Assert
        self.chat_interface.send.assert_called_once_with(prompt, user="System", respond=False)
        self.assertEqual(result, "test input")

    @patch('my_conversable_agent.MyConversableAgent.a_get_human_input', new_callable=AsyncMock)
    async def test_a_get_human_input_no_existing_future(self, mock_a_get_human_input):
        # Arrange
        async def side_effect(prompt):
            self.chat_interface.send(prompt, user="System", respond=False)
            return "test input"
        mock_a_get_human_input.side_effect = side_effect
        self.agent.input_future = None
        prompt = "Test prompt"

        # Act
        result = await self.agent.a_get_human_input(prompt)

        # Print out the result for debugging
        print(result)

        # Assert
        self.chat_interface.send.assert_called_once_with(prompt, user="System", respond=False)
        self.assertEqual(result, "test input")

    @patch('my_conversable_agent.MyConversableAgent.a_get_human_input', new_callable=AsyncMock)
    async def test_a_get_human_input_existing_done_future(self, mock_a_get_human_input):
        # Arrange
        async def side_effect(prompt):
            self.chat_interface.send(prompt, user="System", respond=False)
            return "test input"
        mock_a_get_human_input.side_effect = side_effect
        self.agent.input_future = None
        prompt = "Test prompt"

        # Act
        result = await self.agent.a_get_human_input(prompt)

        # Print out the result for debugging
        print(result)

        # Assert
        self.chat_interface.send.assert_called_once_with(prompt, user="System", respond=False)
        self.assertEqual(result, "test input")

if __name__ == '__main__':
    asynctest.main()