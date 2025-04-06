import streamlit as st
import requests
import os

st.title("BisuGPT using OpenRouter")

user_input = st.text_input("Ask BisuGPT anything:")

if user_input:
    api_key = os.getenv("OPENROUTER_API_KEY")  # Set this in your secrets
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://your-domain.com",  # Put your website or GitHub link
        "X-Title": "BisuGPT"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # or "openai/gpt-4" etc.
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        st.write(reply)
    else:
        st.error("Something went wrong. Check your API key or model choice.")
