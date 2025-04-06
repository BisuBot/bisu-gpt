import streamlit as st
import requests
import os

st.set_page_config(page_title="BisuGPT", layout="centered")
st.title("BisuGPT - Powered by OpenRouter")

api_key = os.getenv("OPENROUTER_API_KEY")  # Must be set in Streamlit secrets
model = "openrouter/openai/gpt-3.5-turbo"  # Or "openrouter/meta-llama/llama-3-8b-instruct"

# User input
user_input = st.text_area("Ask BisuGPT anything:", height=150)

if st.button("Send"):
    if not api_key:
        st.error("API Key not found. Please set OPENROUTER_API_KEY in Streamlit secrets.")
    elif not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("BisuGPT is thinking..."):
            try:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }

                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are BisuGPT, a helpful AI."},
                        {"role": "user", "content": user_input}
                    ]
                }

                response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                         headers=headers, json=payload)

                result = response.json()

                if "choices" not in result:
                    st.error("Error from OpenRouter:")
                    st.code(result)  # Show full error
                else:
                    reply = result["choices"][0]["message"]["content"]
                    st.markdown("**BisuGPT says:**")
                    st.success(reply)

            except Exception as e:
                st.error("Something went wrong.")
                st.code(str(e))
