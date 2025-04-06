import os
import openai

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

response = openai.ChatCompletion.create(
    model="openrouter/openai/gpt-3.5-turbo",  # Use this exact model name
    messages=[
        {"role": "system", "content": "You are BisuGPT, a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
