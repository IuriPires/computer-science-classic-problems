from functools import lru_cache

# lru_cache decorator memoizes the function automatically
# for us. It allows us to keep the origanal recursive implementation
# while python memoizes the function by itself
@lru_cache(maxsize=None)
def fibonnaciMagic(n: int) -> int:
    if n < 2:
        return n
    return fibonnaciMagic(n - 1) + fibonnaciMagic(n - 2)

print(fibonnaciMagic(21))