from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chat = client.chats.create(model="gemini-3.5-flash-lite")
# response = chat.send_message("What is the weather currently in Hyderabad")

# print(response.text)
from google.genai import types

# 1. Define your function (Adding a docstring helps the model understand what it does)
def get_weather(location: str):
    """Get the current weather for a given location."""
    return {"location": location, "temperature": 25, "unit": "celsius", "condition": "sunny"}

# 2. Initialize the chat and pass the raw function inside the config
# chats = client.chats.create(
#     model="gemini-3.5-flash-lite",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant. Provide answers in plain text only. Do not use any Markdown formatting, asterisks, bullet points, or bold text.",
#         tools=[get_weather],
#     )
# )

# response = chats.send_message("What is the weather currently in Hyderabad")
# print(response.text)

# print("#############")
# print(response.model_dump_json(indent=2))

chats = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant. Provide answers in plain text only. Do not use any Markdown formatting, asterisks, bullet points, or bold text.",
        tools=[get_weather],
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    ))
response = chats.send_message("What is the weather currently in Hyderabad")   
# print(response.model_dump_json(indent=2))
if response.function_calls:
    print("Function call detected:")
    print(response.function_calls)
    for tool_call in response.function_calls:
        print(f"Tool Name: {tool_call.name}")
        print(f"Arguments: {tool_call.args}")
        