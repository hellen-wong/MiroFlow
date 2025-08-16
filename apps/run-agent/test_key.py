import requests
import os

# Store your API key in an environment variable for safety
# export OPENROUTER_API_KEY="your_api_key_here"

API_KEY = "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"
if not API_KEY:
    raise ValueError("Missing OpenRouter API key. Set OPENROUTER_API_KEY env variable.")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": "anthropic/claude-3.7-sonnet",  # Claude via OpenRouter
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello Claude, can you hear me?"}
    ],
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    print("Claude replied:\n", data["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)

