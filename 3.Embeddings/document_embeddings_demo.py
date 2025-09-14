from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions= 64)
documents = [
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France.",
    "Tokyo is the capital of Japan.",
    "Canberra is the capital of Australia."
]
vectors = embeddings.embed_documents(documents)
query = "Information about Kolkata."
print(query)
query_vector = embeddings.embed_query(query)
similarities = cosine_similarity([query_vector], vectors)[0]
index, similarity = sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1]
print(f"Most similar document: {documents[index]} (Similarity: {similarity})")
