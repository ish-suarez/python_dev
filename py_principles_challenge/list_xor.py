def list_xor(n,  list1, list2):
    if n not in list1  and n not in list2:
        return False
    if n in list1 and n in list2:
        return False 
    return True
    
    
print(list_xor(1, [1, 2, 3], [4, 5, 6]))


# # smart solution: uses the built-in xor operator ^
# def list_xor(n, list1, list2):
#     return (n in list1) ^ (n in list2)

# # naive solution: check each case at a time
# def list_xor(n, list1, list2):
#     if n not in list1 and n not in list2:
#         return False
#     if n in list1 and n in list2:
#         return False
#     return True

# def list_xor(n,  list1, list2):
#     if n in list1:
#         if n in list2:
#             return False
#         return True
#     if n in list2:
#         if n in list1:
#             return False
#         return True
#     return False