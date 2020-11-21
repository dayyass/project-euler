from utils import find_divisors


def problem_012(n_divisors: int = 500) -> int:
    """
    Iterate over triangle numbers in a loop while exceed n_divisors.

    - O(1) space-complexity
    """
    cnt = 0
    triangle_number = 0
    while len(find_divisors(triangle_number)) <= n_divisors:
        cnt += 1
        triangle_number += cnt
    return triangle_number


if __name__ == '__main__':
    print(f'Problem 12 solution: {problem_012()}')
