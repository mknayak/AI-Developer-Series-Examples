from ai_clients import AIClient, AIConfig, AIPrompt, AIRequest, SenderType
from dotenv import load_dotenv
import os
load_dotenv()


config = AIConfig(
    api_key=os.environ["API_KEY"],
    model="gpt-4.1-mini",
    base_url=os.environ["BASE_URL"],
)
client = AIClient(
    name="AI Bot",
    config=config,
    save_conversation=True
)
continue_conversation = True
while continue_conversation:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        continue_conversation = False
        print("Exiting the conversation.")
        break
    if user_input.lower() == "reset":
        client.reset_conversation()
        print("Conversation has been reset.")
        continue
    request = AIRequest(messages=[
        AIPrompt(role=SenderType.SYSTEM, content="You are a helpful assistant. Give the crisp answer only. No additional information."),
        AIPrompt(role=SenderType.USER, content=user_input),
    ])

    response = client.send_message(request)
    print(f"AI Response: {response.response} [Tokens Used: Input - {response.input_tokens}, Output - {response.output_tokens}, Total - {client.total_tokens_used}]") 