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