def x_and_o(string):
    num_of_o = len([ x for x in string if x == 'x' ])
    num_of_x = len([ o for o in string if o == 'o' ])
    return num_of_o == num_of_x

print(x_and_o('xxoo'))