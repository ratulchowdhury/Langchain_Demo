from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os
load_dotenv()

print("Loading local Hugging Face model...")

try:
    # For local models, we don't need the API token parameter
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # A smaller conversational model
        task="text-generation",
        # Remove huggingfacehub_api_token for local models
        pipeline_kwargs={
            "max_new_tokens": 100, 
            "temperature": 0.7,
            "do_sample": True,
            "pad_token_id": 50256
        }
    )
    
    print("Creating chat model...")
    model = ChatHuggingFace(llm=llm)
    
    print("Making inference...")
    result = model.invoke("What is the capital of West Bengal?")
    print("\n" + "="*50)
    print("Response:", result.content)
    print("="*50)
    
except Exception as e:
    print(f"Error: {e}")
    print("\nThis might be due to:")
    print("- Model still downloading (first run takes time)")
    print("- Memory constraints")
    print("- Try a smaller model like distilgpt2")