"""
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python
"""
# My solution:
def find_uniq(arr):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    a, b, c = arr[:3]
    n = b
    if a == b or a == c: 
        n = a
        
    for element in arr:
        if element != n: return element

# Solution by eqlion https://www.codewars.com/kata/reviews/5941972edacd78ae0a00013c/groups/5942ce6bb4513a72e4000218
def find_uniq(arr):
    """
    Summary time complexity: O(2*n)
    Space complexity: O(n)
    """
    a, b = set(arr) # O(n)
    return a if arr.count(a) == 1 else b # O(n)
