from typing import Set, Iterable


def arithmetic_series_multiple_of_d_up_to_upper_bound(d: int, upper_bound) -> int:
    """
    Sum of natural numbers up to upper_bound multiples of d.
    - O(1) time-complexity
    - O(1) space-complexity
    """
    n = (upper_bound - 1) // d
    S = d * n * (n + 1) // 2
    return S


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


def find_all_divisors(n: int) -> Set[int]:
    all_divisors = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            all_divisors.add(i)
            all_divisors.add(n // i)
    return all_divisors


def product(iterable: Iterable):
    product = 1
    for i in iterable:
        product *= i
    return product
