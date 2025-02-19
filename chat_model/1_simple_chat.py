from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

result = model.invoke("What is 20 divided by 10?")
print("Full result:")
print(result)
print("content only:")
print(result.content)