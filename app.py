import streamlit as st
from openai import OpenAI

# Load your API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.title("BisuGPT - Your Office Buddy")

user_input = st.text_input("Type your question to BisuGPT...")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are BisuGPT, an expert office assistant who knows everything about office politics, PNIR rules, and claims work."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(response.choices[0].message.content)
