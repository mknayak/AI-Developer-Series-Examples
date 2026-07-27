from typing import Protocol
from openai import OpenAI
import os 
import time
from dotenv import load_dotenv 
load_dotenv()
    
class LLMClient(Protocol):
    def create(**kwargs) -> dict:
        ...



class OpenAIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
    
    def create(self, **kwargs) -> dict:
        return self.client.responses.create(**kwargs)
    
class TestClient:
    def __init__(self):
        ...
    def create(self, **kwargs) -> dict:
        time.sleep(2)
        return {"response": "Test response"}
    def other_method(self):
        return "This is another method in TestClient"

def send_message(client:LLMClient, prompt: str, **kwargs) -> str:
    # thread wait for 2 seconds to simulate a request to OpenAI API 
    time.sleep(2)
    client.create(**kwargs)
    print(f"Sending message to {client.__class__.__name__}: {prompt}")
    return f"OpenAI response to '{prompt}'"

if __name__ == "__main__":   
    open_ai_key = os.environ["API_KEY"]
    base_url = os.environ["BASE_URL"]

    client = OpenAIClient(base_url=base_url, api_key=open_ai_key)
    client.create(
        model="gpt-4.1-mini",
        input=[{"role": "user", "content": "Hello!"}]
    )
    send_message(client, "Hello!", model="gpt-4.1-mini", input=[{"role": "user", "content": "Hello!"}]) 
    
    #testing
    test_client = TestClient()
    send_message(test_client, "Hello!", model="gpt-4.1-mini")