from utils import find_proper_divisors


def check_amicable_number(n: int) -> bool:
    """
    Check if the number is amicable.

    - O(sqrt(n)) time-complexity
    - O(n) space-complexity
    """
    d_n = sum(find_proper_divisors(n) - {n})
    if n == d_n:
        return False
    d_dn = sum(find_proper_divisors(d_n) - {d_n})
    if n == d_dn:
        return True
    return False


def problem_021(upper_bound: int = 10000) -> int:
    """
    For every number under n check if it amicable number.

    - O(n * sqrt(n)) time-complexity
    - O(n^2) space-complexity
    """
    result = 0
    for n in range(2, upper_bound):
        if check_amicable_number(n):
            result += n
    return result


if __name__ == '__main__':
    print(f'Problem 21 solution: {problem_021()}')
