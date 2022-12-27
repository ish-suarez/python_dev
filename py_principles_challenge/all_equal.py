def all_equal(arr):
    return all(item == arr[0] for item in arr)
print(all_equal([]))

# def all_equal(array):
#     if len(array) < 1:
#         return True
#     return len(set(array)) == 1

# print(all_equal([1, 1]))


# naive solution
# def all_equal(items):
#     for item1 in items:
#         for item2 in items:
#             if item1 != item2:
#                 return False
#     return True


# # one-liner with nested list comprehension
# # and the all() built-in
# def all_equal(items):
#     return all(item1 == item2 for item1 in items for item2 in items)