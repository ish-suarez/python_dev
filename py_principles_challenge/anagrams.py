# Challenge
# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.

def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
    

print(is_anagram("typhoon", "opython"))