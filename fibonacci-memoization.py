from typing import Dict

memo: Dict[int, int] = { 0: 0, 1: 1 }

def fibonacciMemo(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacciMemo(n - 1) + fibonacciMemo(n - 2)
    return memo[n]


print(fibonacciMemo(10))
