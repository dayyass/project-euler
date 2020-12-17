from utils import sum_of_digit_powers_in_number


def find_upper_bound(power: int) -> int:
    """
    Helper function to find upper search bound.
    """
    n = 1
    while n <= len(str(n * 9 ** power)):
        n += 1
    return 10 ** n


def problem_030(power: int = 5) -> int:
    """
    Sum all suitable numbers up to upper bound.

    - O(2^n) time-complexity
    - O(1) space-complexity
    """
    result = 0
    upper_bound = find_upper_bound(power)
    for n in range(2, upper_bound):
        if n == sum_of_digit_powers_in_number(n, power):
            result += n
    return result


if __name__ == '__main__':
    print(f'Problem 30 solution: {problem_030()}')
