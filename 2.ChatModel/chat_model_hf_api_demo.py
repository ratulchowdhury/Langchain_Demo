from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

# Check if HF API token is available
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
if not hf_token:
    print("Error: HUGGINGFACE_API_TOKEN not found in environment variables.")
    print("Please check your .env file has: HUGGINGFACE_API_TOKEN=your_token_here")
    exit(1)

print(f"Using HF token: {hf_token[:10]}...")

try:
    print("Initializing Hugging Face endpoint...")
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen3-Next-80B-A3B-Instruct", 
        task="text-generation",
        huggingfacehub_api_token=hf_token,
        timeout=30
    )
    
    print("Creating chat model...")
    model = ChatHuggingFace(llm=llm, temperature=0.5)
    
    print("Making request to Hugging Face API...")
    result = model.invoke("What is the capital of West Bengal?")
    print("Response:", result.content)
    
except Exception as e:
    error_msg = str(e)
    print(f"Error occurred: {error_msg}")
    
    if "503" in error_msg or "Service Temporarily Unavailable" in error_msg:
        print("\n🚨 The Hugging Face inference service is temporarily unavailable.")
        print("This is a server-side issue, not a problem with your code or API key.")
        print("Please try again in a few minutes.")
        print("\nAlternatively, you can use the OpenAI demo which is working:")
        print("python .\\chat_model_openai_demo.py")
    elif "401" in error_msg or "authentication" in error_msg.lower():
        print("\n🔑 Authentication error. Please check your API token.")
    else:
        print("\n💡 For a working example, try the OpenAI demo:")
        print("python .\\chat_model_openai_demo.py")
