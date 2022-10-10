"""
https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python
"""
def valid_braces(string):
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for bracket in string:
        if bracket in pairs.keys():
            if len(stack) == 0: return False
            if pairs[bracket] != stack.pop():
                return False
        elif bracket in pairs.values():
            stack.append(bracket)
    return not(len(stack))
