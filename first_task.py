"""First task - caching Fibonacci"""


from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """
    Returns the internal fibonacci function used 
    to compute Fibonacci numbers using caching
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Computes Fibonacci numbers.

        Args:
        n (int): The n-th Fibonacci number.

        Returns:
        int: The value of n-th Fibonacci number
        """

        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


fib = caching_fibonacci()

print(fib(20))
print(fib(5))
