def format_number(num):
    if num >= 0:
        return '{:,}'.format(num)
        
print(format_number(1000000))


# # DIY solution
# def format_number(n):
#     result = ""
#     for i, digit in enumerate(reversed(str(n))):
#         if i != 0 and (i % 3) == 0:
#             result += ","
#         result += digit
#     return result[::-1]