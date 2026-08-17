from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, ValidationInfo, field_validator, model_validator


app = FastAPI(title="Day 10 FastAPI Demo")


class UserCreate(BaseModel):
	name: str = Field(min_length=2, max_length=50)
	age: int = Field(ge=18, le=120)
	email: EmailStr
	password: str = Field(min_length=8, max_length=100)
	confirm_password: str = Field(min_length=8, max_length=100)
 
	@field_validator("confirm_password")
	@classmethod
	def passwords_match(cls, v: str, info: ValidationInfo):
		password = info.data.get("password")
		if password is None or v != password:
			raise ValueError("Passwords do not match")
		return v
	
	# validated after all fields are validated
	@model_validator(mode="after")
	def validate_class(self):
		if self.password in self.email:
			raise ValueError("Password should not contain email")
		return self

class UserResponse(BaseModel):
	message: str
	user: UserCreate


@app.get("/")
def read_root() -> dict[str, str]:
	return {"message": "FastAPI is running"}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate) -> UserResponse:
	return UserResponse(message="User validated successfully", user=user)



#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app)

# run using fastapi dev api.py --reload