responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

def basic_tests():
    print(len(responses))
    print(responses[0])
    print(responses[-1])

def list_slicing():
    #list[start_index:end_index:step] end_index is exclusive
    slice = responses[1:3]
    print(slice)
    print(responses[:2])
    print(responses[2:])

    print(responses[::2])  # Every second item

def list_mutation():
    batch = responses.copy()
    batch.append({"id": "msg_5", "text": "New response", "tokens": 10, "finish_reason": "end_turn"})
    print(len(batch))
    print(len(responses))

    responses[0]["text"] = "Updated text"
    print(batch[0]["text"])
    print(responses[0]["text"])

    removed_item= batch.pop(2)
    print(removed_item)  # Output: {'id': 'msg_3', '

    more_resopnses = [
        {"id": "msg_6", "text": "Another response", "tokens": 15, "finish_reason": "end_turn"},
        {"id": "msg_7", "text": "Yet another response", "tokens": 20, "finish_reason": "end_turn"},
    ]

    batch.extend(more_resopnses)
    print(len(batch))

def list_comprehension():
    ids = [r["id"] for r in responses]
    print(ids)

    tokens = [r["tokens"] for r in responses if r["tokens"] > 0]
    print(tokens)

    filtered_texts = [r["text"] for r in responses if r["text"] is not None]
    print(filtered_texts)

list_comprehension()

