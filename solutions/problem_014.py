from utils import collatz_sequence_len


def problem_014(upper_bound: int = 1_000_000) -> int:
    """
    Straightforward solution. Iterate over numbers in a loop while collatz_sequence_len exceed upper_bound.

    - O(1) space-complexity
    """
    max_len = 0
    result = 0
    for i in range(1, upper_bound):
        collatz_len_i = collatz_sequence_len(i)
        if collatz_len_i > max_len:
            max_len = collatz_len_i
            result = i
    return result


if __name__ == '__main__':
    print(f'Problem 14 solution: {problem_014()}')
