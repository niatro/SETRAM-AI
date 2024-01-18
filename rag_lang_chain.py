import os
import pinecone
from langchain.chat_models import ChatOpenAI
from config import open_api_key, pinecone_api_key
import time
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader



chat = ChatOpenAI(
    openai_api_key=open_api_key,
    model='gpt-3.5-turbo'
)

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="Hi AI, how are you today?"),
#     AIMessage(content="I'm great thank you. How can I help you?"),
#     HumanMessage(content="Que es interesante de los modelos LLM lama")
# ]
# res = chat(messages)
# print(res.content)

# get API key from app.pinecone.io and environment from console
pinecone.init(
    api_key=pinecone_api_key,
    environment='us-east1-gcp' 
)



index_name = 'setram-01'

# if index_name not in pinecone.list_indexes():
#     pinecone.create_index(
#         index_name,
#         dimension=1536,
#         metric='cosine'
#     )
#     # wait for index to finish initialization
#     while not pinecone.describe_index(index_name).status['ready']:
#         time.sleep(1)

index = pinecone.Index(index_name)
print(index.describe_index_stats())

embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")
loader = UnstructuredPDFLoader("manual_vial.pdf")
data = loader.load()
print (f'Tenemos {len(data)} documento(s) en nuestra data')
print (f'Hay {len(data[0].page_content)} caracteres en nuestro documento')