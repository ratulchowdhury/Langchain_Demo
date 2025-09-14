from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
documents = [
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France.",
    "Tokyo is the capital of Japan."
]
# text = "Kolkata is the capital of West Bengal."

vectors = embeddings.embed_documents(documents)
print(len(vectors))

