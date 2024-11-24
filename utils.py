from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os


MODEL_NAME = "llama-3.1-70b-versatile"

try:
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])


pirate_to_english_prompt = """
                            You are a translator whose role is to translate Pirate-Speak to Modern-day English
                            Here are a few examples:
                            1. Ahoy Matey = Hello there
                            2. Aye aye, Captain = Yes sir
                            3. Savvy? = Do you understand?

                            The next Pirate-Speak is the one you need to translate:\n
                            """

english_to_pirate_prompt = """
                            You are a translator whose role is to translate English to Pirate-Speak
                            Here are a few examples:
                            1. Hello, my name is John = Ahoy! Me name be John
                            2. Woah! = Shiver me timbers!
                            3. Pay attention = Avast ye

                            The next English phrase is the one you need to translate:\n
                            """
def get_translation(text, is_pirate_speak):    
    if(is_pirate_speak):
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": pirate_to_english_prompt+text
                }
            ],
            temperature=0,
            stop=None,
        )
        return completion.choices[0].message.content

    else:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": english_to_pirate_prompt+text
                }
            ],
            temperature=0,
            stop=None,
        )
        return completion.choices[0].message.content