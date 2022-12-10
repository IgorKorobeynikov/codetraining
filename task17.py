"""
https://www.codewars.com/kata/541c8630095125aba6000c00
"""

def digital_root(n: int) -> int:
    if n < 10: return n
    return digital_root(sum(map(int, str(n))))
