from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_completion_tokens=250, timeout=None)
result = llm.invoke("What is the capital of West Bengal?")
print(result.content)