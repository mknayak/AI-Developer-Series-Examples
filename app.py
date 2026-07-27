import os
from dotenv import load_dotenv
load_dotenv()

open_ai_key = os.getenv("OPEN_AI_KEY")
base_url = os.getenv("BASE_URL")

print("Welcome to TechWayFit")
print(f"Your OpenAI Key is: {open_ai_key}")
print(f"Your Base URL is: {base_url}")