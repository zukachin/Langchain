from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

chat_history = [] 

system_message = SystemMessage(content="You are a fanatasy story teller.")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print("------resultwithothertokensusage-------")
    print(result)

    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)

