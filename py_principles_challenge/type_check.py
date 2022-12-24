def only_ints(a, b):
    return type(a) == int and type(b) == int

print(only_ints('1', 2))