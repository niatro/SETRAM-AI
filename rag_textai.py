## 1. Semantic Search ##
from txtai import Embeddings
from leer_data import data
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from tokenizers import Tokenizer
import torch
from txtai.pipeline import LLM


# Sample data for indexing 

embeddings = Embeddings(path="sentence-transformers/nli-mpnet-base-v2")
embeddings.index(data)

print("Busqueda semantica:")
for query in ["Que factores se ven impactados en una red vial deteriorada ", "Rodados en la via, ¿Cual es el peligro?"]:
    uid = embeddings.search(query, 1)[0][0]
    print(f"Pregunta: {query}, Resultado: {data[uid]}")


## 4. Keyword Search and Dense Vector index ##

# Create embeddings with subindexes
# embeddings = Embeddings(
#   content=True,
#   defaults=False,
#   indexes={
#     "keyword": {
#       "keyword": True
#     },
#     "dense": {
#       "path": "sentence-transformers/nli-mpnet-base-v2"
#     }
#   }
# )
# embeddings.index(data)
# print("Keyword & Dense Index Search Results:")
# for query in ["Cacofonia"]:
#   print(f"Query: {query}, Keyword Result: ")    
#   print(embeddings.search(query, limit=1, index="keyword"))
#   print("Dense Index Result: ")
#   print(embeddings.search(query, limit=1, index="dense"))

## 5. Hybrid Search (Sparse + Dense) ##
# print("\nHybrid Search Results:")
# hybrid_embeddings = Embeddings(hybrid=True, path="sentence-transformers/nli-mpnet-base-v2")
# hybrid_embeddings.index(data)
# for query in ["Cacofonia"]:
#     uid = hybrid_embeddings.search(query, 1)[0][0]
#     print(f"Query: {query}, Result: {data[uid]}")

## 6. Content Storage for large amount of data ##

# print("\nTest de almacenamiento:")
# content_embeddings = Embeddings(content=True, path="sentence-transformers/nli-mpnet-base-v2")
# content_embeddings.index(data)
# uid = int(content_embeddings.search("señales de peligro", 1)[0]["id"])
# print("Result:", data[uid])
    
## 8. Using LLM  ##

# llm = LLM("google/flan-t5-large", torch_dtype=torch.float32)
# query = "2+2?"
# result = llm(query)
# print("LLM Standalone Result:")
# print("Query: ", query, result)

## 9. RAG (Retrieval-Augmented Generation) ##
# from txtai.pipeline import Extractor

# llm_embeddings = Embeddings(path="sentence-transformers/nli-mpnet-base-v2", content=True, autoid="uuid5")
# llm_embeddings.index(data)

# extractor = Extractor(llm_embeddings, "google/flan-t5-large")

# llm_query = "Que factores se ven impactados en una red vial deteriorada?"
# context = lambda question: [{"query": question, "question": f"Answer the following question using the context below.\nQuestion: {question}\nContext:"}]
# print("RAG Result:")
# print(extractor(context(llm_query))[0])