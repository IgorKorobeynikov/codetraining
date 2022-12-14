"""
https://www.codewars.com/kata/515f51d438015969f7000013
"""

def pyramid(n: int) -> list[list[int]]:
    return [[1 for j in range(1, i + 1)] for i in range(1, n + 1)]
