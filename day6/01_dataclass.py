from dataclasses import dataclass,asdict
from enum import Enum

#Simple Class
class AIChatMessage:
    def __init__(self, sender: str, message: str, timestamp: str):
        self.sender = sender
        self.message = message
        self.timestamp = timestamp

    def is_system(self) -> bool:
        return self.sender.lower() == "system"

user_message2 = AIChatMessage(sender="User", message="Hello, how are you?", timestamp="2024-06-01 10:00:00")
print(user_message2)
print(user_message2.__dict__)

# Dataclass - Mutable by default
# Define a data class for similar behavior.
# dataclasses automatically generate __init__, __repr__, and other methods, making it easier to work with classes that primarily store data.
@dataclass
class ChatMessage:
    sender: str
    message: str
    timestamp: str
    
    def is_system(self)-> bool:
        return self.sender.lower() == "system"

user_message = ChatMessage(sender="User", message="Hello, how are you?", timestamp="2024-06-01 10:00:00")
print(user_message)
print(f"Is system message: {user_message.is_system()}")

system_message = ChatMessage(sender="System", message="I am a chatbot. How can I assist you?", timestamp="2024-06-01 10:00:05")
print(system_message)
print(f"Is system message: {system_message.is_system()}")

# Dataclass - Immutable (frozen=True)
# adding frozen=True makes the dataclass immutable, meaning its attributes cannot be changed after instantiation. This is useful for creating objects that should not be modified once created, ensuring data integrity and preventing accidental changes.
@dataclass(frozen=True)
class ChatMessageFrozen:
    sender: str
    message: str
    timestamp: str

    def is_system(self) -> bool:
        return self.sender.lower() == "system"

#system_message.message="Please provide your account number for verification."
#print(system_message)

#Enum for sender type
# Using an Enum for the sender type provides a clear and restricted set of possible values for the sender attribute, enhancing code readability and reducing the risk of errors due to typos or invalid values. It also allows for more structured handling of sender types in the code.
class SenderType(Enum):
    USER = "User"
    SYSTEM = "System"

@dataclass(frozen=True)
class ChatMessageWithEnum:
    sender: SenderType
    message: str
    timestamp: str
    
    def is_system(self) -> bool:
        return self.sender == SenderType.SYSTEM
    
user_message_enum = ChatMessageWithEnum(sender=SenderType.USER, message="Hello, how are you?", timestamp="2024-06-01 10:00:00")
print(user_message_enum)
print(f"Is system message: {user_message_enum.is_system()}")
print(user_message_enum.__dict__)  #print as dictionary
print(asdict(user_message_enum))  #print as dictionary using asdict

# Data class with additional methods and properties
# property decorator allows you to define methods that can be accessed like attributes, providing a way to compute values on-the-fly while keeping the interface clean and intuitive. This is useful for derived attributes that depend on other fields of the dataclass.
@dataclass(frozen=True)
class ChatResponse:
    response: str
    confidence: float
    timestamp: str
    input_tokens: int
    output_tokens: int

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens
    
    def is_confident(self) -> bool:
        return self.confidence > 0.8

# Data class for model configuration
# default values for the fields provide a convenient way to create instances with common settings, while still allowing for customization when needed. This is particularly useful for configuration objects where certain parameters have standard defaults but can be overridden as necessary.

@dataclass(frozen=True)
class ModelConfig:
    model_name: str = "gpt-4"
    max_tokens: int = 1000
    temperature: float = 0.7
    top_p: float = 0.9
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0

config = ModelConfig()
print(config)
config2 = ModelConfig(model_name="gpt-3.5", max_tokens=500, temperature=0.5)
print(config2)

@dataclass
class ChatSession:
    session_id: str
    user_id: str
    messages: list[ChatMessage]
    config: ModelConfig

    def add_message(self, message: ChatMessage):
        self.messages.append(message)

    def get_last_message(self) -> ChatMessage | None:
        return self.messages[-1] if self.messages else None

session = ChatSession(session_id="session_001", user_id="user_123", messages=[], config=config)
session.add_message(user_message)
session.add_message(system_message)
print(session)
#end dataclass examples