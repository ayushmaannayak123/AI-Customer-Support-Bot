# llm.py

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0.3
)


def generate_response(prompt: str) -> str:
    """
    Sends the prompt to the local Ollama model.
    """
    response = llm.invoke(prompt)
    return response.content