# Challenge
# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter,
# which is a string. Your function should return a list of all
# the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(string):
    indexes = []
    for i, character in enumerate(string):
        if character.isupper():
            indexes.append(i)
    return indexes
print(capital_indexes('HeLlO'))

from string import ascii_uppercase as uppercase
def capital_indexes(string):
    return [i for i in range(len(string)) if string[i] in uppercase]

print(capital_indexes('HeLlO'))