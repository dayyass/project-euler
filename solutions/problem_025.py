from utils import fibonacci_generator


def problem_025(n_digits: int = 1000) -> int:
    """
    Compute fib numbers up to n_digits length.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    for i, num in fibonacci_generator():
        if len(str(num)) >= n_digits:
            return i


if __name__ == '__main__':
    print(f'Problem 25 solution: {problem_025()}')
