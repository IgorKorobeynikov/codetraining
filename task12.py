"""
https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/
"""

def hex_string_to_RGB(hex_string: str) -> dict[str, int]:
    return {c:b for c, b in zip("rgb", bytearray.fromhex(hex_string.replace("#", "")))}
