from dataclasses import dataclass
from enum import Enum
from urllib import response
import requests

@dataclass(frozen=True)
class AIConfig:
    api_key: str
    model: str
    base_url: str

class SenderType(Enum):
    USER = "user"
    SYSTEM = "system"

@dataclass
class AIPrompt:
    role: SenderType
    content: str

@dataclass
class AIRequest:
    messages: list["AIPrompt"]    

@dataclass  
class AIResponse:
    response: str
    has_error: bool = False
    input_tokens: int = 0
    output_tokens: int = 0
    
class AIClient:
    def __init__(self, name: str, config: AIConfig, save_conversation: bool = False):
        self.name = name
        self.config = config
        self.save_conversation = save_conversation
        self.previous_response_id = None
        self.total_tokens_used = 0  # Initialize total tokens used

    def send_message(self, request: AIRequest) -> AIResponse:        
        ai_request = {
            "model": self.config.model,
            "input": [{"role": prompt.role.value, "content": prompt.content} for prompt in request.messages]
        }
        if self.previous_response_id:
            ai_request["previous_response_id"] = self.previous_response_id
        ai_request_url = f"{self.config.base_url}/responses"
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json"
        }
       # print(f"Sending request to {ai_request_url} with payload: {ai_request}")
        response = requests.post(ai_request_url, json=ai_request, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: Received response {response.status_code} - {response.text}")
            return AIResponse(response=f"Error: {response.status_code} - {response.text}", has_error=True)
        
        response_json = response.json() 
        
        #print(f"Received response: {response.status_code} - {response.text}")
        ai_response = AIResponse(
            response=response_json["output"][0]["content"][0]["text"] if response.status_code == 200 else f"Error: {response.status_code} - {response.text}",
            has_error=False,
            input_tokens=response_json.get("usage", {}).get("input_tokens", 0),
            output_tokens=response_json.get("usage", {}).get("output_tokens", 0)
        )
        if response.status_code == 200:
            self.total_tokens_used += response_json.get("usage", {}).get("total_tokens", 0)
        
        if self.save_conversation:
            self.previous_response_id = response_json.get("id", None)
        return ai_response

    def reset_conversation(self):
        self.previous_response_id = None
        self.total_tokens_used = 0  # Reset total tokens used
        
    def receive_message(self, message):
        print(f"{self.name} received: {message}")