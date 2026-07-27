
responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]


def example_list_comprehensions():
    complete = [r for r in responses if r["finish_reason"] == "end_turn"]
    print([r["id"] for r in complete])
    texts = [r["text"] for r in responses if r["text"] is not None]
    print(texts)
    long_responses = [{"id": r["id"], "word_count": len(r["text"].split())} for r in responses if r["text"] and r["tokens"] > 40]
    print(long_responses)


def example_nested_comprehension():
    retrieved_chunks = [["chunk1a", "chunk1b"], ["chunk2a"], ["chunk3a", "chunk3b", "chunk3c"]]
    all_chunks = [chunk for chunk_list in retrieved_chunks for chunk in chunk_list]
    print(all_chunks)


def example_dict_and_set_comprehensions():
    response_map = {r["id"]: r["text"] for r in responses if r["text"]}
    print(response_map)
    token_bands = {"high" if r["tokens"] >= 40 else "low" for r in responses}
    print(token_bands)


example_list_comprehensions()
#example_nested_comprehension()
#example_dict_and_set_comprehensions()

