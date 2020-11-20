# https://projecteuler.net/problem=1


# O(n) solution
def problem_01(upper_bound: int = 1000):
    """
    Straightforward solution suitable in time.
    """
    return sum(i for i in range(upper_bound) if (i % 3 == 0) or (i % 5 == 0))


# O(1) solution
def problem_01_faster(upper_bound: int = 1000):
    """
    Constant time solution using arithmetic series.
    1) add sum of natural numbers up to 1000 multiples of 3;
    2) add sum of natural numbers up to 1000 multiples of 5;
    3) subtract sum of natural numbers up to 1000 multiples of 15, since for these numbers 1) and 2) occur twice.
    """
    S_3 = arithmetic_series_multiple_of_d(3, upper_bound=upper_bound)
    S_5 = arithmetic_series_multiple_of_d(5, upper_bound=upper_bound)
    S_15 = arithmetic_series_multiple_of_d(15, upper_bound=upper_bound)
    return S_3 + S_5 - S_15


def arithmetic_series_multiple_of_d(d: int, upper_bound: int = 1000):
    """
    Sum of natural numbers up to upper_bound multiples of d.
    """
    n = (upper_bound - 1) // d
    S = d * n * (n + 1) // 2
    return S


if __name__ == '__main__':
    print(f'problem 1 solution: {problem_01_faster()}')
