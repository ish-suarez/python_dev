def just_numbers(mixed_list):
    return [ x for x in mixed_list if type(x) == int ]
    
print(just_numbers([1, 'dd', 7, 'ewe', 4, 'edn', 6]))