import streamlit as st 
import requests import os

st.set_page_config(page_title="BisuGPT - Powered by Meta LLaMA 4") st.title("BisuGPT") st.write("A custom AI chatbot powered by Meta's LLaMA 4 model via OpenRouter.")

Get the API key from Streamlit secrets

OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]

Define the OpenRouter API endpoint

API_URL = "https://openrouter.ai/api/v1/chat/completions"

Sidebar for model selection and API info

with st.sidebar: st.markdown("Powered by: Meta LLaMA 4") st.markdown("Model: openrouter/meta-llama/llama-4")

Chat input and conversation history

if "messages" not in st.session_state: st.session_state.messages = []

Display previous messages

for msg in st.session_state.messages: role = "You:" if msg["role"] == "user" else "BisuGPT:" st.markdown(f"{role} {msg['content']}")

User input

prompt = st.chat_input("Type your message here...")

if prompt: st.session_state.messages.append({"role": "user", "content": prompt}) headers = { "Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json" } data = { "model": "openrouter/meta-llama/llama-4", "messages": st.session_state.messages, }

response = requests.post(API_URL, headers=headers, json=data)
if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.markdown(f"**BisuGPT:** {reply}")
else:
    st.error("Something went wrong. Please try again.")
