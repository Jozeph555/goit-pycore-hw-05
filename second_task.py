"""Second task - number generator"""


import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Parses the text and genarates number generator

    Args:
    text (str): The text that contains the real
    numbers (the parts of income).

    Returns:
    Generator[float, None, None]: The generator of numbers.
    """

    numbers = re.findall(r"\d+\.\d+", text)

    for number in numbers:
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculates total income using 
    generator_numbers function

    Args:
    text (str): The text that contains the real
    numbers (the parts of income).
    func (Callable): The function that processes 
    the data and generates the number generator.

    Returns:
    float: Sum of all numbers (total profit) from
    number generator.
    """

    profit = sum(func(text))

    return profit


SOME_TEXT = """Загальний дохід працівника складається з
 декількох частин: 1000.01 як основний дохід, доповнений 
 додатковими надходженнями 44.45 і 324.00 доларів."""

total_income = sum_profit(SOME_TEXT, generator_numbers)

print(f"Total income: {total_income}")
