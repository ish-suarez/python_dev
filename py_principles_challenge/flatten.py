def flatten(array):
        return [ item for sub_array in array for item in sub_array ]
    
    
print(flatten([[1, 2], [3, 4], [5], [6]]))