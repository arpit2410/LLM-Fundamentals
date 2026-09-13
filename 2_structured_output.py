from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from pydantic import BaseModel
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chats = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant. Provide answers in plain text only. Do not use any Markdown formatting, asterisks, bullet points, or bold text."
#     )
# )
# response = chats.send_message("Give me name, age, and occupation of a fictional person")
# print(response.text)
# chats = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant. Provide answers in structured JSON format only. Do not use any Markdown formatting, asterisks, bullet points, or bold text."
#     ))

# response = chats.send_message("Give me name, age, and occupation of a fictional person")
# print(response.text)

# "Response in structured JSON format only" in the prompt is a suggestion to the model, but it may not always follow the instruction. To ensure that the model's output is in a structured format, we can use the `response_schema` parameter in the `send_message` method. This allows us to define a schema for the expected response, and the model will generate output that adheres to this schema.

class Person(BaseModel):
    name: str
    age: int
    occupation: str

# 1. Initialize the chat with your system instructions
chats = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful assistant. Do not use any Markdown formatting, asterisks, bullet points, or bold text."
    )
)

# 2. Pass the schema and mime_type inside a config block specifically for this message
response = chats.send_message(
    "Give me name, age, and occupation of a fictional person", 
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Person,
    )
)

# 3. Use response.parsed to access the Pydantic object directly
person_data = response.parsed


print(f"Name: {person_data.name}")
print(f"Age: {person_data.age}")
print(f"Occupation: {person_data.occupation}")