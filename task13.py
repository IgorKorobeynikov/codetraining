"""
https://www.codewars.com/kata/52fea6fd158f0576b8000089
"""

class Converter(object):
    @staticmethod
    def to_ascii(h: str) -> str:
        return bytes.fromhex(h).decode()
    @staticmethod
    def to_hex(s: str) -> str:
        return bytes(s, "ascii").hex()
