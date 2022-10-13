def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

        # Going down through the recursion until reach base case
        # fibonacci(4 - 1) ; fibonacci(4-2)
        # fibonacci(3 - 1) ; fibonacci(3 - 2)
        # fibonacci(2 - 1) ; fibonacci(1 - 2)

        # Going up through the base case until first item of the call stack summing up the results
        # (fibonacci(2 - 1) = 1 ; fibonacci(1 - 2) = 1) = 2
        # (fibonacci(3 - 1) = 2 ; fibonacci(3 - 2) = 1) = 3
        # (fibonacci(4 - 1) = 3 ; fibonacci(4 - 2) = 2) = 5
        # (fibonacci(5 - 1) = 5 ; fibonacci(5 - 2) = 3) = 8

        # Fibonacci(5) = 8


print(fibonacci(8))