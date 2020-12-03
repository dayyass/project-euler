def problem_016(n: int = 1000) -> int:
    """
    Straightforward solution.
    """
    return sum(int(digit) for digit in str(2**n))


if __name__ == '__main__':
    print(f'Problem 16 solution: {problem_016()}')
