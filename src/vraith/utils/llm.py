from langchain_mistralai import ChatMistralAI
from vraith.config.settings import (
    MISTRAL_API_KEY,
    MODEL_NAME,
    MODEL_TEMPERATURE,
)

def get_llm(): 
    return ChatMistralAI(
            api_key=MISTRAL_API_KEY,
            model=MODEL_NAME,
            temperature=MODEL_TEMPERATURE,
        )