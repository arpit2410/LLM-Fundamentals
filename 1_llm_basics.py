import json
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

# Create the Gemini API client using the API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------------------------------------------------
# 1. Basic Chat Session
# ---------------------------------------------------------

# Create a chat session instead of directly using generate_content
chat = client.chats.create(model="gemini-3.5-flash-lite")

# Send a message to the chat session
response = chat.send_message("What is the square root of 16?")

# Print the model's response
# print(response.text)
print(response.model_dump_json(indent=2))
# print(response)

# ---------------------------------------------------------
# 2. Chat with System Instructions
# ---------------------------------------------------------

# Create a chat session with a system instruction
# The system instruction defines the assistant's behavior
# chat = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant."
#     )
# )

# Send a message to the model
# result = chat.send_message("What is the square root of 16?")

# Print the response
# print(result.text)


# ---------------------------------------------------------
# 3. Chat with Conversation History
# ---------------------------------------------------------

# Create a chat session with previous conversation history
# This allows the model to understand previous messages
# chat = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant."
#     ),
#     history=[
#         {"role": "user", "parts": [{"text": "My Name is Arpit. I am a software engineer."}]},
#         {"role": "model", "parts": [{"text": "Nice to meet you, Arpit!"}]}
#     ])

# Send a new message while maintaining the previous context
# result = chat.send_message("Can you tell me about the latest trends in software engineering?")

# Print the response
# print(result.text)


# ---------------------------------------------------------
# 4. Chat Configuration: System Instruction + Temperature
# ---------------------------------------------------------

# Create a chat session with custom model behavior
# temperature controls the randomness/creativity of responses
# Higher temperature = more creative/random responses
# chat = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant who cracks jokes and makes people laugh.",
#         temperature=0.7,
#         # max_output_tokens=100
#     )
# )

# Send a message to the model
# result = chat.send_message("Can you tell me a joke about software engineers?")

# Print the response
# print(result.text)

# Display token usage information
# print("Tokens used:", result.usage_metadata.total_token_count)
# print("Input tokens:", result.usage_metadata.prompt_token_count)
# print("Output tokens:", result.usage_metadata.candidates_token_count)


# ---------------------------------------------------------
# 5. Streaming Response
# ---------------------------------------------------------

# Create a chat session for streaming responses
# Streaming allows the response to be displayed as it is generated
# streaming_chat = client.chats.create(
#     model="gemini-3.6-flash",
#     config=types.GenerateContentConfig(
#         system_instruction="You are a helpful assistant who cracks jokes and makes people laugh.",
#         temperature=0.7,
#         # max_output_tokens=100
#     )
# )

# Send the message and receive the response in chunks
# result = streaming_chat.send_message_stream(
#     "Can you tell me a joke about software engineers?"
# )

# Print each chunk immediately as it arrives
# for chunk in result:
#     print(chunk.text, end="", flush=True)