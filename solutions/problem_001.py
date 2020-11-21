def arithmetic_series_multiple_of_d_up_to_upper_bound(d: int, upper_bound) -> int:
    """
    Sum of natural numbers up to upper_bound multiples of d.

    - O(1) time-complexity
    - O(1) space-complexity
    """
    n = (upper_bound - 1) // d
    S = d * n * (n + 1) // 2
    return S


def problem_001(upper_bound: int = 1000) -> int:
    """
    Straightforward solution suitable in time.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    return sum(i for i in range(upper_bound) if (i % 3 == 0) or (i % 5 == 0))


def problem_001_faster(upper_bound: int = 1000) -> int:
    """
    Constant time solution using arithmetic series.
    1) add sum of natural numbers up to 1000 multiples of 3;
    2) add sum of natural numbers up to 1000 multiples of 5;
    3) subtract sum of natural numbers up to 1000 multiples of 15, since for these numbers 1) and 2) occur twice.

    - O(1) time-complexity
    - O(1) space-complexity
    """
    S_3 = arithmetic_series_multiple_of_d_up_to_upper_bound(3, upper_bound=upper_bound)
    S_5 = arithmetic_series_multiple_of_d_up_to_upper_bound(5, upper_bound=upper_bound)
    S_15 = arithmetic_series_multiple_of_d_up_to_upper_bound(15, upper_bound=upper_bound)
    return S_3 + S_5 - S_15


if __name__ == '__main__':
    print(f'Problem 1 solution: {problem_001_faster()}')
