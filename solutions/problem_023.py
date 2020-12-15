from typing import List
from utils import find_proper_divisors


def find_all_abundant_numbers(upper_bound: int = 28124) -> List[int]:
    """
    Find all abundant_numbers below upper_bound.

    - O(n * sqrt(n)) time-complexity
    - O(n) space-complexity
    """
    all_abundant_numbers = []
    for n in range(1, upper_bound):
        if n < sum(find_proper_divisors(n)):
            all_abundant_numbers.append(n)
    return all_abundant_numbers


def problem_023(upper_bound: int = 28124) -> int:
    """
    1) find all abundant_numbers below upper_bound;
    2) find sum of all possible pairs of abundant_numbers;
    3) check if the sum below upper_bound and add to set;
    4) subtract from sum of all numbers below upper_bound sum of elements in set 4).

    - O(n * sqrt(n)) time-complexity
    - O(n) space-complexity
    """
    sum_of_abundant_numbers_set = set()
    all_abundant_numbers = find_all_abundant_numbers(upper_bound)
    for i in all_abundant_numbers:
        for j in all_abundant_numbers:
            sum_ij = i + j
            if sum_ij < upper_bound:
                sum_of_abundant_numbers_set.add(sum_ij)
    result = sum(range(upper_bound)) - sum(sum_of_abundant_numbers_set)
    return result


if __name__ == '__main__':
    print(f'Problem 23 solution: {problem_023()}')
