import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():

    print("Creating Groq LLM")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )