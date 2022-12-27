from math import floor

# def mid(string):
#     is_there_middle = len(string) % 2
#     middle = floor(len(string) / 2)
#     switcher = {
#         0: '',
#         1: string[middle]
#     }

#     return switcher.get(is_there_middle)
# mid('aaoaa')



def mid(string):
    has_middle = len(string) % 2 == 0
    middle_character = len(string) // 2
    if has_middle:
        return ""
    elif has_middle == False:
        return string[middle_character]

    
print(mid('aaoaa'))