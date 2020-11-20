# https://projecteuler.net/problem=2


def problem_02(upper_bound: int = 4_000_000):
    """
    - O(n) time-complexity
    - O(1) space-complexity

    Compute fib numbers in a loop, adding even-values terms to result.
    """
    result = 0  # cumulative sum
    fib_1 = 0  # prev fib number
    fib_2 = 1  # next fib number
    while fib_1 + fib_2 <= upper_bound:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        if fib_2 % 2 == 0:
            result += fib_2
    return result


if __name__ == '__main__':
    print(f'Problem 2 solution: {problem_02()}')
