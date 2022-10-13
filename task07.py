"""
https://www.codewars.com/kata/54edbc7200b811e956000556/python
"""
def count_sheeps(sheep):
    return sum(filter(lambda n: type(n) == bool, sheep))
