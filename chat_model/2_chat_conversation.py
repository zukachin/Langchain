from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

result = model.invoke(messages)
print(result)
print(f"Answer from AI: {result.content}")


'''
There are 3 types of messages here:
SystemMessage: Like the domain person (Ok now you are a super python developer)
HumanMessage: we users
AIMessage: the reply that model give us

**Note the systemmessage should be first**

'''