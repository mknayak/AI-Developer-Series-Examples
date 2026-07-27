from abc import ABC, abstractmethod
import time
class LLMClientBase(ABC):
    @abstractmethod
    def send_request(self, prompt: str) -> str:
        pass
    

class OpenAIClient(LLMClientBase):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def send_request(self, prompt: str) -> str:
        # thread wait for 2 seconds to simulate a request to OpenAI API 
        time.sleep(2)
        return f"OpenAI response to '{prompt}' using model '{self.model}'"

class AnthropicClient(LLMClientBase):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def send_request(self, prompt: str) -> str:
        # thread wait for 2 seconds to simulate a request to Anthropic API 
        time.sleep(2)
        return f"Anthropic response to '{prompt}' using model '{self.model}'"

class AzureOpenAIClient(LLMClientBase):
    def __init__(self, api_key: str, model: str, endpoint: str):
        self.api_key = api_key
        self.model = model
        self.endpoint = endpoint

    def send_request(self, prompt: str) -> str:
        # thread wait for 2 seconds to simulate a request to Azure OpenAI API 
        time.sleep(2)
        return f"Azure OpenAI response to '{prompt}' using model '{self.model}' at endpoint '{self.endpoint}'"
    
    
#classmethod, staticmethod, and instance methods in LLMManager class
class LLMManager:
    clients: dict[str, LLMClientBase]={}
    def __init__(self, client_name: str): 
        self.client_name = client_name
    
    @classmethod
    def get_llm_client(cls, client_name: str) -> LLMClientBase:
        return cls.clients[client_name]
    @classmethod
    def register_llm_client(cls, client_name: str, client: LLMClientBase):
        cls.clients[client_name] = client 
        
    @staticmethod    
    def llm_client(client_name: str, base_url,key,model) -> LLMClientBase:
        if client_name == "openai":
            client = OpenAIClient(api_key=key, model=model)
        elif client_name == "anthropic":
            client = AnthropicClient(api_key=key, model=model)
        elif client_name == "azure_openai":
            client = AzureOpenAIClient(api_key=key, model=model, endpoint=base_url)
        else:
            raise ValueError(f"Unknown client name: {client_name}")
        
        return client

    def send_request(self, prompt: str) -> str:
        client = self.get_llm_client(self.client_name)
        return client.send_request(prompt)
    

if __name__ == "__main__":
    client= LLMManager.llm_client("openai", base_url="", key="dummy_key", model="gpt-4.1-mini")
    response = client.send_request("Hello, how are you?")
    print(response)
    
    #register the clients
    LLMManager.register_llm_client("openai", OpenAIClient(api_key="dummy_key", model="gpt-4.1-mini"))
    LLMManager.register_llm_client("anthropic", AnthropicClient(api_key="dummy_key", model="claude-v1"))
    LLMManager.register_llm_client("azure_openai", AzureOpenAIClient(api_key="dummy_key", model="gpt-4.1-mini", endpoint="https://example.com"))
    
    #1
    client_1_response = LLMManager("openai").send_request("Hello from OpenAI!")
    print(client_1_response)
    #2
    client_2_response = LLMManager("anthropic").send_request("Hello from Anthropic!")
    print(client_2_response)
    #3
    client_3_response = LLMManager("azure_openai").send_request("Hello from Azure OpenAI!")
    print(client_3_response)
    
    
    
    
    