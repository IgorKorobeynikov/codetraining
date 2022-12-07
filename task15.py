"""
https://www.codewars.com/kata/515decfd9dcfc23bb6000006/
More about ipaddress library: https://docs.python.org/3/library/ipaddress.html
It could also be solved using regular expressions and in other ways
"""
def is_valid_IP(ip: str) -> bool:
    try:
        __import__("ipaddress").ip_address(ip)
    except ValueError as exc:
        return False
    return True
