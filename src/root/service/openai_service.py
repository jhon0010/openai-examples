import datetime
import os
import openai 
from openai import OpenAI

"""
Created with version: openai==1.3.5.

A class to interact with the OpenAI API.

This class is a wrapper around the OpenAI API.
    * It allows to get a simple chat with a context.
"""
class OpenAIService:

    DAVINCI_TEXT_MODEL = "text-davinci-003"
    GPT3_MODEL = 'gpt-3.5-turbo'
    GPT4_TURBO_MODEL = 'gpt-4-1106-preview'
    CURRENT_MODEL = GPT4_TURBO_MODEL

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY", "not-found")

    """
    A function to generate a chat getted a prompt and a list of messages.
    Allowing to create a simple chat with a context.

    For this we are using the OpenAI API call chat completions, for more information see:
    
        https://platform.openai.com/docs/guides/text-generation/chat-completions-api

    """
    def simple_chat(self):

        messages=[
                {
                    "role": "system",
                    "content": "You are a helpful chatbot assitant.",
                }
            ]

        while True:
            message = input("User : ")
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                client = OpenAI(api_key=openai.api_key)
                chat = client.chat.completions.create(
                    model=OpenAIService.CURRENT_MODEL, messages=messages
                )
            print(chat)
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            messages.append({"role": "assistant", "content": reply})


            # save messages to a file (chat history)
            with open(f'chat_history {datetime.datetime.now()}.txt', "w") as f:
                for message in messages:
                    f.write({message})