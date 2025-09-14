from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()   

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions= 64)
documents = [
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France.",
    "Tokyo is the capital of Japan."
]

vectors = embeddings.embed_documents(documents)
print(len(vectors))