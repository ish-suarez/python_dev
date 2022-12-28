# Challenge
# Solution validation
# The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

# Write a function named validate that takes code represented as a string as its only parameter.

# Your function should check a few things:

# the code must contain the def keyword
# otherwise return "missing def"
# the code must contain the : symbol
# otherwise return "missing :"
# the code must contain ( and ) for the parameter list
# otherwise return "missing paren"
# the code must not contain ()
# otherwise return "missing param"
# the code must contain four spaces for indentation
# otherwise return "missing indent"
# the code must contain validate
# otherwise return "wrong name"
# the code must contain a return statement
# otherwise return "missing return"
# If all these conditions are satisfied, your code should return True.

# Here comes the twist: your solution must return True when validating itself.

def validate(string):
    break_points = ['def', 'validate', '(', ')', ':', 'return', '    ']
    matches = [x for x in break_points if x in string]
    if 'def' not in matches:
        return 'missing def'
    if ':' not in matches:
        return 'missing :'
    if '(' and ')' not in matches:
        return 'missing paren'
    if '(' + ')' in string:
        return 'missing param'
    if '    ' not in matches:
        return 'missing indent'
    if 'validate' not in string:
        return 'wrong name'
    if 'return' not in matches:
        return 'missing return'
    return True
    
code_to_validate = "def validate(string):\n break_points = ['def', 'validate', '(', ')', ':','return', '    ']\n matches = [x for x in break_points if x in string]\n if 'def' not in matches:\n return 'missing def'\n if ':' not in matches:\n return 'missing :'\n if '(' and ')' not in matches:\n return 'missing paren'\n if '(' + ')' in string:\n return 'missing param'\n if ' ' not in matches:\n return 'missing indent'\n if 'validate' not in string:\n return 'wrong name'\n if 'return' not in matches:\n return 'missing return'\n return True"
print(validate(code_to_validate))