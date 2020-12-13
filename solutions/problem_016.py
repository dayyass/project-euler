from utils import sum_of_digits_in_number


def problem_016(n: int = 1000) -> int:
    """
    Straightforward solution.
    """
    return sum_of_digits_in_number(2**n)


if __name__ == '__main__':
    print(f'Problem 16 solution: {problem_016()}')
