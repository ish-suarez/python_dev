def add_dots(string):
    for i in range(len(string) - 1):
            return '.'.join(string[i:])
    return string

print(add_dots('test'))

def remove_dots(string):
    for i in range(len(string) - 1):
        return string.replace('.', '')
    return string

print(remove_dots('t.e.s.t'))

print(remove_dots(add_dots('test')))
