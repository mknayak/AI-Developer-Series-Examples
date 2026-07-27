message_dict={
    "id": "msg_1",
    "text": "Hello user, how are you?",
    "sender": "user_1",
    "timestamp": "2024-06-01T12:00:00Z"
}

def basic_dict_test():
    print(len(message_dict))
    print(message_dict["id"])
    print(message_dict["text"])
    print(message_dict.get("sender"))
    print(message_dict.get("nonexistent_key", "default_value")) 
    print("id" in message_dict)
    print("nonexistent_key" in message_dict)
    #dict check value exists
    print("user_1" in message_dict.values())
    print("nonexistent_value" in message_dict.values())

def dict_slicing():
    keys_to_slice = ["id", "text"]
    sliced_dict = {k: message_dict[k] for k in keys_to_slice} 
    print(sliced_dict)  

def dict_comprehension():
    # Dictionary Comprehension
    # {key: value for key, value in iterable if condition}
    uppercased_dict = {k: (v.upper() if isinstance(v, str) else v) for k, v in message_dict.items()}
    print(uppercased_dict)
    filtered_dict = {k: v for k, v in message_dict.items() if isinstance(v, str) and "user" in v}
    print(filtered_dict)
    nested_dict = {
        "message": message_dict,
        "metadata": {
            "length": len(message_dict["text"]),
            "contains_user": "user" in message_dict["sender"]
        }
    }
    print(nested_dict)
    filtered_nested_dict = {
        "message": {k: v for k, v in message_dict.items() if isinstance(v, str) and "user" in v},
        "metadata": {
            "length": len(message_dict["text"]),
            "contains_user": "user" in message_dict["sender"]
        }
    }
    print(filtered_nested_dict)  # Output: {'message': {'sender': 'user_1'}, 'metadata': {'length': 18, 'contains_user': True}}
    list_of_list_str=[["user_1","user_2"],["user_3","user_4"],["user_5"]]
    total_users=[user for sublist in list_of_list_str for user in sublist]
    print(total_users)




#basic_dict_test()
#dict_slicing()
dict_comprehension()
