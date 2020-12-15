from utils import fibonacci_generator


def problem_002(upper_bound: int = 4_000_000) -> int:
    """
    Compute fib numbers up to upper bound, adding even-values terms to result.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    result = 0  # cumulative sum
    for _, num in fibonacci_generator():
        if num > upper_bound:
            break
        if num % 2 == 0:
            result += num
    return result


if __name__ == '__main__':
    print(f'Problem 2 solution: {problem_002()}')
