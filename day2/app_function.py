import os
import openai
from dotenv import load_dotenv
load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")
base_url = os.getenv("BASE_URL")

def chat_message(role:str,message:str):
    return {"role": role, "content": message}; 
def call_llm(client, messages:list, model_choice:str="gpt-4.1-mini"):
    system_prompt = "You are a helpful assistant that provides concise and accurate answers to user queries.";
    messages.append(chat_message("system", system_prompt));
    response = client.chat.completions.create(
        model=model_choice,
        messages=messages
    );
    return response.choices[0].message;

def call_llm_2(client, *messages, model_choice:str="gpt-4.1-mini"):
    messages = list(messages)
    response = client.chat.completions.create(
        model=model_choice,
        messages=messages
    );
    return response.choices[0].message;

def call_llm_3(client, *messages, **args):
    messages = list(messages)
    response = client.chat.completions.create(
        messages=messages,
        **args
    );
    return response.choices[0].message;


client = openai.OpenAI(base_url=base_url, api_key=open_ai_key)
system_prompt = "You are a helpful assistant that provides concise and accurate answers to user queries.";
response = call_llm_3(client, 
                      chat_message("user",input("You: ")),
                      chat_message("system",system_prompt),
                      model="gpt-4.1-mini",
                      temperature=0.7
                      );

print(response.content)