import streamlit as st
import openai
import os

# Load API key from Streamlit secrets
openai.api_key = st.secrets["OPENROUTER_API_KEY"]
openai.api_base = "https://openrouter.ai/api/v1"

# Optional: Add custom headers
openai.requestssession = openai.requests.Session()
openai.requestssession.headers.update({
    "HTTP-Referer": "https://bisubot.streamlit.app",  # Change to your actual app URL
    "X-Title": "BisuGPT"
})

# Streamlit app UI
st.title("BisuGPT")
st.markdown("Ask anything to your friendly assistant!")

user_input = st.text_input("Enter your question:")

if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",  # Or "anthropic/claude-2", etc.
            messages=[
                {"role": "system", "content": "You are BisuGPT, a smart and helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")
