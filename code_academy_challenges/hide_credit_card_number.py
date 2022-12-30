def hide_number(num):
    return '*'*(len(num) - 4) + num[-4:]

print(hide_number("4444444444441234"))