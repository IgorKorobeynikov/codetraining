"""
EN: Write a `recursion_limit` decorator that will limit the recursion depth for the function
RU: Написать декоратор `recursion_limit`, который будет ограничивать глубину рекурсии для функции

```
@recursion_limit(depth=100)
def func(n):
    if n == 0: return
    return func(n-1)
```

"""

def recursion_limit(depth=1000):
    def wrapper_(func):
        level = -1
        def wrapper(*args, **kwargs):
            nonlocal level
            level += 1
            if level <= depth:
                result = func(*args, **kwargs)
                return result
            raise RecursionError(f"Recursion depth exceeded. More than {depth} calls")
        return wrapper
    return wrapper_

@recursion_limit(depth=2)
def count_down(n):
    if n == 0:
        return "STOP"
    return count_down(n-1)
print(count_down(2))

# count_down(2) depth = 0
# count_down(1) depth = 1
# count_down(0) depth = 2
