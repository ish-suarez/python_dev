def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
    

print(is_anagram("typhoon", "opython"))