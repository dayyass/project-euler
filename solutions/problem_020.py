from utils import factorial, sum_of_digits_in_number


def problem_020(n: int = 100) -> int:
    """
    Straightforward solution.
    """
    return sum_of_digits_in_number(factorial(n))


if __name__ == '__main__':
    print(f'Problem 20 solution: {problem_020()}')
