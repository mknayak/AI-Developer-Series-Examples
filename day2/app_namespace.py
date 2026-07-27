from services.LLMClient import llm_response
from openai import OpenAI

response = llm_response("Explore TechWayFit.com blogs and summarize in 3 lines?")

client = OpenAI(base_url="https://api.openai.com/v1", api_key="YOUR_API_KEY")
print(response)