# 1. Write a Python program to check if a given positive integer is a power of two
def power_of_two(num):
    return int(num) % 2 == 0
print(power_of_two(4)) # True

# 2. Write a Python program to check if a given positive integer is a power of three.
def power_of_three(num):
    return int(num) % 3 == 0
print(power_of_three(9)) # True

# 3. Write a Python program to check if a given positive integer is a power of four.
def power_of_four(num):
    return int(num) % 4 == 0
print(power_of_four(4)) # True

# 4. Write a Python program to check if a number is a perfect square.
from math import sqrt
def perfect_square(num):
    return int(sqrt(num) + 0.5)**2 == num
print(perfect_square(9)) # True

# 5. Write a Python program to check if an integer is the power of another integer.
from math import log
def both_powers(x, y):
    power = log(int(x), int(y))
    return (y**power) == x
print(both_powers(128,2)) # True
print(both_powers(127,2)) # False

# 7. Write a Python program to find a missing number from a list.
def missing_number(num_array):
    return sum(range(num_array[0], num_array[-1] + 1)) - sum(num_array)
print(missing_number([ 100, 102, 103 ]))

# 8. Write a Python program to find missing numbers from a list.
def find_missing_nums(num_array):
    return [ i for x, y in zip(num_array, num_array[1:])
                for i in range(x + 1, y) if y - x > 1 ]
print(find_missing_nums([1,2,5,6,8]))
