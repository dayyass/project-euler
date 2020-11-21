def problem_006(n: int = 100) -> int:
    """
    Compute the loop using one loop, instead of straightforward solution with two loops.

    - O(n) time-complexity
    - O(1) space-complexity
    """
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(n + 1):
        square_of_sum += i
        sum_of_squares += i**2
    return square_of_sum**2 - sum_of_squares


if __name__ == '__main__':
    print(f'Problem 6 solution: {problem_006()}')
