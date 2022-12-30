def calculator(num1, op, num2):
    if op == 'and':
        return num1*num2
    if op == '+':
        return num1+num2
    if op == '-':
        return num1 - num2
    if op == '/':
        return num1 / num2
    
print(calculator(6, 'and', 4))