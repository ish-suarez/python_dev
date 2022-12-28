# Challenge
# Boolean and
# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(x, y, z):
    return x and y and z == True

print(triple_and(True, True, False))

# Alternate
# def triple_and(a, b, c):
#     return a and b and c