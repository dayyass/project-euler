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


def is_pandigital(n: int) -> bool:
    """
    Check if the number is pandigital.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    str_n = str(n)
    for i in range(1, len(str_n) + 1):
        if str(i) not in str_n:
            return False
    return True


def is_leap_year(year: int) -> bool:
    """
    Check if year is leap.

    - O(1) time-complexity
    - O(1) space-complexity
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))


def sum_of_digits_in_number(n: int) -> int:
    """
    Calculate the sum of the digits in the number.
    """
    return sum(int(digit) for digit in str(n))


def sum_of_digit_powers_in_number(n: int, power: int) -> int:
    """
    Calculate the sum of the digits in the number.
    """
    return sum(int(digit) ** power for digit in str(n))


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


def factorial(n: int) -> int:
    """
    Calculates the factorial of a number
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


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


def find_proper_divisors(n: int) -> Set[int]:
    """
    Find all proper divisors of a number.
    - O(sqrt(n)) time-complexity
    - O(n) space-complexity
    """

    divisors = find_divisors(n)
    return divisors - {n}  # without n


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


def fibonacci_generator():
    """
    Fibonacci numbers generator that yields position of the number and number itself.
    """
    fib_prev = 0  # prev fib number
    fib_cur = 1  # next fib number
    i = 1  # number position
    while True:
        yield i, fib_cur
        i += 1
        fib_prev, fib_cur = fib_cur, fib_prev + fib_cur


def prime_generator():
    """
    Prime numbers generator that yields position of the number and number itself.
    """
    i = 0  # prime numbers counter
    num = 0  # current number
    while True:
        num += 1
        if is_prime(num):
            i += 1
            yield i, num
