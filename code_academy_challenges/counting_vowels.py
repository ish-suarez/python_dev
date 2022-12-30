def counting_vowels(word):
    vowels = [ 'a', 'e', 'i', 'o', 'u' ]
    found_vowels = [ x for x in vowels if x in word ]
    return len(found_vowels)

print(counting_vowels('Hello'))