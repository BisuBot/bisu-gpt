import streamlit as st
import requests
import os

st.set_page_config(page_title="BisuGPT using Meta LLaMA 4", page_icon="🤖")
st.title("BisuGPT using Meta LLaMA 4 via OpenRouter")

st.markdown("Ask BisuGPT anything:")

prompt = st.text_input("")

api_key = os.getenv("OPENROUTER_API_KEY")
model = "meta-llama/llama-4"

if prompt:
    if not api_key:
        st.error("API key not found. Please set the environment variable `OPENROUTER_API_KEY`.")
    else:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
            result = response.json()
            reply = result["choices"][0]["message"]["content"]
            st.markdown("**BisuGPT says:**")
            st.success(reply)
        except Exception as e:
            st.error(f"Error: {e}")
