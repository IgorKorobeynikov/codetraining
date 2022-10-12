"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""

move_zeros = lambda lst: sorted(lst, key = lambda n: float('inf') if not n else 0)
"""
Space complexity: O(n)
Time complexity: O(n log n)
"""
