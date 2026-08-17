# Types are hints — ignored at runtime
def summarize_test(text: str, max_tokens: int) -> str: 
    print(f"text:{text}, max_tokens: {max_tokens}")
    return text

def summarize(text: str, max_tokens: int) -> str: 
    response= text[:max_tokens] + "..." if len(text) > max_tokens else text
    print(response)
    return response

#mypy strict=true will give an error for the following function, as it is not implemented, but will run without error
def extract_keywords(text: str) -> list: ...

def score_responses(    responses: list[str]) -> dict[str, float]:
    return {response: len(response) for response in responses}

summarize_test(100,10) #typecheck fails but can run, as no runtime error
summarize("100",10) #typecheck fails: positional argument follows keyword argument
