message_set = {"msg_1", "msg_2", "msg_3"}
another_set = {"msg_2", "msg_3", "msg_4", "msg_4"}
message_hash_set = set(["msg_1", "msg_2", "msg_3"]) 


def basic_set_test():
    print(len(message_set))
    print(len(another_set))
    print("msg_1" in message_set)
    print("msg_4" in message_set)

def set_operations():
    another_set = {"msg_2", "msg_3", "msg_4"}
    print(message_set.union(another_set))
    print(message_set.intersection(another_set))
    print(message_set.difference(another_set)) 
    print(message_set.symmetric_difference(another_set))


def set_operations_2():
    another_set = {"msg_2", "msg_3", "msg_4"}
    print(message_set | another_set)
    print(message_set & another_set)
    print(message_set - another_set)
    print(message_set ^ another_set) 

#basic_set_test()
#set_operations()
set_operations_2()
