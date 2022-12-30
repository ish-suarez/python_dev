def repeat_char(string):
    new = ''
    for i in string:
        new = new + i*2
    return new
        
    
print(repeat_char('now'))