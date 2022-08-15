from functools import lru_cache

@lru_cache(maxsize=2000)
def fibonacci(n: int) -> int:
    if n==0:
        return 0
    elif n<3:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 