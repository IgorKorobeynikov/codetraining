"""
https://www.codewars.com/kata/523f5d21c841566fde000009/python
"""
def array_diff(a, b):
    """
    Time complexity - O(n)
    """
    diff = []
    sb = set(b) 
    for value in a:
        if value not in sb: diff.append(value)
    return diff
