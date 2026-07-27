import os
import openai
from dotenv import load_dotenv
load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")
base_url = os.getenv("BASE_URL")

client = openai.OpenAI(base_url=base_url, api_key=open_ai_key)
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": input("You: ")}
    ]
)
print(response.choices[0].message.content)