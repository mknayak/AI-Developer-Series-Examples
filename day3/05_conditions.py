#sample LLM Response list
from random import choices


responses = [
    {"id": "resp1", "finish_reason": "end_turn", "choices": [{"text": "The capital of France is Paris.", "index": 0, "logprobs": None, "finish_reason": "end_turn"}]},
    {"id": "resp2", "finish_reason": "max_tokens",  "choices": [{"text": "The response was truncated due to token limit.", "index": 0, "logprobs": None, "finish_reason": "max_tokens"}]},
    {"id": "resp3", "finish_reason": "stop_sequence", "choices": [{"text": "The model stopped generating text.", "index": 0, "logprobs": None, "finish_reason": "stop_sequence"}]},
    {"id": "resp4", "finish_reason": "stop", "choices": [{"text": "The model stopped for an unknown reason.", "index": 0, "logprobs": None, "finish_reason": "stop"}]},
]

def classify_finish_reason(response):
    reason = response.get("finish_reason", "unknown")
    if reason == "end_turn":
        return "complete"
    elif reason == "max_tokens":
        return "truncated"
    elif reason == "stop_sequence":
        return "stopped"
    else:
        return f"unknown: {reason}"

#index-based loop (not recommended in Python, but common in C#)
for i in range(len(responses)):
    print(classify_finish_reason(responses[i]))

# For-each (preferred)
for r in responses:
    print(classify_finish_reason(r))

# With index (preferred over range+len)
for i, r in enumerate(responses):
    print(f"{i}: {classify_finish_reason(r)}")

#using comprehensions to create a list of classifications
classifications = [classify_finish_reason(r) for r in responses]
#using comprehensions to create a dict of id:classification
id_to_classification = {r["id"]: classify_finish_reason(r) for r in responses}

# zip — pair two lists together
prompts = ["What is RAG?", "Explain embeddings", "What is a token?"]
model_outputs = ["RAG is...", "Embeddings are...", "A token is..."]

for prompt, output in zip(prompts, model_outputs):
    print(f"Q: {prompt}\nA: {output}\n")


# Iterating dict items (extremely common with JSON responses)
response_meta = {"model": "claude-3-5-sonnet", "usage": {"input_tokens": 100, "output_tokens": 250}}
for key, value in response_meta.items():
    print(f"{key}: {value}")


# Early exit with break
for r in responses:
    if r.get("finish_reason") == "max_tokens":
        print(f"Warning: {r['id']} was truncated!")
        break  # stop after first truncated response