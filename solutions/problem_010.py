from utils import prime_generator


def problem_010(upper_bound: int = 2_000_000) -> int:
    """
    Straightforward solution using prime_generator.

    - O(n^(3/2)) time-complexity
    - O(1) space-complexity
    """
    result = 0
    for i, num in prime_generator():
        if num >= upper_bound:
            break
        result += num
    return result


if __name__ == '__main__':
    print(f'Problem 10 solution: {problem_010()}')
