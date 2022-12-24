def double_letters(string):

    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return True
    return False
    
print(double_letters('Success'))



# def double_letters(string):
#     return any([a == b for a, b in zip(string, string[1:])])