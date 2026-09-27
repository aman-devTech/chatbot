from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-3.6-flash")
messages = [

]
print("------welcome (0 to exit)------")
while True:
    prompt= input("YOU : ")
    messages.append(prompt)
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(response.text)
    print("BOT : ",response.text)
print(messages)