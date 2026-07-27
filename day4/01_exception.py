from tenacity import retry,stop_after_attempt,wait_fixed,retry_if_exception_type

class SimulatedException(Exception):
    pass

def function_that_may_fail():
    print("Trying to execute the function...")
    raise SimulatedException("An error occurred!")

def function_fail():
    print("Trying to execute the function...")
    raise Exception("An error occurred!")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception_type(SimulatedException))    
def call_llm():
    print("Calling LLM...")
    function_that_may_fail()
    return "LLM response"


call_llm()