from pydantic import BaseModel, Field, EmailStr
from typing import Annotated


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    user_id: int = Field(gt=0)
    max_tokens: int = Field(gt=0, le=1000)
    input_language: str = Field(min_length=2, max_length=10)
    input_token:int = Field(gt=0, le=1000)
    output_token:int = Field(gt=0, le=1000)

#reuse validation
positive_int = Annotated[int, Field(gt=0,le=1000)]
class ChatRequest2(BaseModel):
    message: str = Field(min_length=1, max_length=500)
    user_id: int = Field(gt=0)
    max_tokens: positive_int
    input_language: str = Field(pattern=r"^[a-z]{2}-[A-Z]{2}$") #en-EN
    input_token:positive_int
    output_token:positive_int
    
    
request = ChatRequest(
    message="Hello, how are you?",
    user_id=123,
    max_tokens=50,
    input_language="English",
    input_token=10,
    output_token=20
)

request2 = ChatRequest2(
    message="Hello, how are you?",
    user_id=123,
    max_tokens=12,
    input_language="en-EN",
    input_token=10,
    output_token=20
)  


print(request)
print(request2)


request3 = ChatRequest2(
    message="Hello, how are you?",
    user_id="123",
    max_tokens=12,
    input_language="en-EN",
    input_token=10,
    output_token=20
)  
print(request3)
print(type(request3.user_id))

#json serialization
print(request.model_dump()) #pydantic v2 method to serialize to dict
print(request.model_dump_json()) #pydantic v2 method to serialize to json

#json deserialization
#class method to create an instance from json string
request4 = ChatRequest.model_validate_json('{"message": "Hello, how are you?", "user_id": 123, "max_tokens": 50, "input_language": "English", "input_token": 10, "output_token": 20}')
print(request4)
