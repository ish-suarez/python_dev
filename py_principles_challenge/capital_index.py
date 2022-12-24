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