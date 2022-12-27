def consecutive_zeros(string):
    return max(map(len, string.split('1')))

print(consecutive_zeros('1001101000110'))


# naive solution
# def consecutive_zeros(bin_str):
#     result = 0
#     streak = 0
#     for letter in bin_str:
#         if letter == "0":
#             streak += 1
#         else:
#             streak = 0
#         result = max(result, streak)
#     return result