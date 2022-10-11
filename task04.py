"""
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
"""
def find_uniq(arr):
    """
    Time complexity: O(n)
    """
    a, b, c = arr[:3]
    n = b
    if a == b or a == c: 
        n = a
        
    for element in arr:
        if element != n: return element
