messages_tuple= ("Hello", "How are you?", "Goodbye","",None)

def basic_tuple_test():
    print(len(messages_tuple))
    print(messages_tuple[0])
    print(messages_tuple[-1])

def tuple_slicing():
    slice = messages_tuple[1:3]
    print(slice)
    slice_ids = [r for r in slice]
    print(slice_ids)

    print(messages_tuple[:2])
    print(messages_tuple[2:])

def tuple_comprehension():
    ids = tuple(r for r in messages_tuple)
    print(ids)

    filtered_texts = tuple(r for r in messages_tuple if r is not None)
    print(filtered_texts)

    list_from_tuple = list(messages_tuple)
    print(list_from_tuple)

    tuple_from_list = tuple(list_from_tuple)
    print(tuple_from_list)


#basic_tuple_test()
#tuple_slicing()
tuple_comprehension()
