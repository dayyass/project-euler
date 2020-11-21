from utils import is_prime


def problem_010(upper_bound: int = 2_000_000) -> int:
    """
    Straightforward solution using loop and is_prime() function.

    - O(n^(3/2)) time-complexity
    - O(1) space-complexity
    """
    result = 0
    for i in range(upper_bound):
        if is_prime(i):
            result += i
    return result


if __name__ == '__main__':
    print(f'Problem 10 solution: {problem_010()}')
