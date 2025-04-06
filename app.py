import streamlit as st
import requests
import os

st.set_page_config(page_title="BisuGPT – Powered by OpenRouter", page_icon="🤖")
st.title("LLaMA 4 via OpenRouter")
st.write("Ask BisuGPT anything:")

prompt = st.text_input("")

if prompt:
    api_key = st.secrets["OPENROUTER_API_KEY"]

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    model = "openrouter/openai/gpt-3.5-turbo"  # <<< USE THIS HERE

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are BisuGPT, a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()

        st.code(result)  # Debug: shows the full raw JSON

        if "choices" not in result:
            st.error(f"Error: 'choices' not found. Full response: {result}")
        else:
            reply = result["choices"][0]["message"]["content"]
            st.markdown("**BisuGPT says:**")
            st.success(reply)

    except Exception as e:
        st.error(f"Exception occurred: {e}")
