"""
https://www.codewars.com/kata/52774a314c2333f0a7000688
"""

def valid_parentheses(string: str) -> bool:
    string = str().join(filter(lambda c: 40 <= ord(c) <= 41 , string))
    try: compile(string, '<string>', 'exec')
    except (SyntaxError, SyntaxWarning): return False
    else: return True
