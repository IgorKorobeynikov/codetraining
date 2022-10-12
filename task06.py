"""
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
"""
# My clumsy solution:
from collections import Counter

def scramble(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    for c in s2:
        if s1[c] < s2[c]: return False
    return True
