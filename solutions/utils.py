from typing import Set, Iterable


def is_prime(n: int) -> bool:
    """
    Check if the number is prime using Trial division algorithm.

    - O(sqrt(n)) time-complexity
    - O(1) space-complexity
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindromic(n: int) -> bool:
    """
    Check if the number is palindromic.

    - O(1) time-complexity
    - O(1) space-complexity
    """
    str_n = str(n)
    if str_n == str_n[::-1]:
        return True
    return False


def find_divisors(n: int) -> Set[int]:
    """
    Find all divisors of a number.
    - O(sqrt(n)) time-complexity
    - O(n) space-complexity
    """
    divisors = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def check_divisible(n: int, divisors: Iterable) -> bool:
    """
    Check if a number is divisible by all numbers in array.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    for i in divisors:
        if n % i != 0:
            return False
    return True


def product(array: Iterable):
    """
    Multiply all elements in array.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    product = 1
    for i in array:
        product *= i
    return product


def collatz_sequence_len(n: int) -> int:
    """
    Compute len of Collatz sequence.

    - O(1) space-complexity
    """
    result = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        result += 1
    return result
