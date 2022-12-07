"""
https://www.codewars.com/kata/57f609022f4d534f05000024
"""

from typing import TypeVar
from collections import Counter
T = TypeVar('T')

def stray(arr: list[T]) -> T:
    return Counter(arr).most_common()[-1][0]
