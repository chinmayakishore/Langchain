import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

# Verify it loaded
print("API key loaded:", api_key[:6], "...")

# Create model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key=api_key
)

# Test prompt
response = llm.invoke("Tell me an easy way to remember all the 50 states of USA")
print(response.content)
