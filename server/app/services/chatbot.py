import openai
import os
from typing import List
from ..models.models import Message


def generate_response(message: str, previous_messages: List[Message]) -> str:
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if openai_api_key:
        try:
            openai.api_key = openai_api_key

            # Prepare context from previous messages
            context = "\n".join(
                [f"{'User' if msg.is_from_user else 'AI'}: {msg.content}" for msg in previous_messages[-5:]])

            prompt = f"""
            You are a helpful assistant in a chat widget application. 
            Here's the recent conversation context:

            {context}

            User: {message}
            AI:"""

            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return generate_generic_response(message)
    else:
        return generate_generic_response(message)


def generate_generic_response(message: str) -> str:
    if "hello" in message.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
