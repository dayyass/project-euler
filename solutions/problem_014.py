from utils import collatz_sequence_len


def problem_014(upper_bound: int = 1_000_000) -> int:
    max_len = 0
    result = 0
    for i in range(1, upper_bound):
        collatz_len_i = collatz_sequence_len(i)
        if collatz_len_i > max_len:
            max_len = collatz_len_i
            result = i
    return result


def problem_014_faster(upper_bound: int = 1_000_000) -> int:
    numner2collatz_sequence_len = {1: 1}
    max_len = 0
    result = 0
    for i in range(1, upper_bound):

        listic = [i]
        while i not in numner2collatz_sequence_len:
            if i % 2 == 0:
                i //= 2
            else:
                i = 3 * i + 1
            listic.append(i)
        
            # result += 1

        collatz_len_i = collatz_sequence_len(i)
        if collatz_len_i > max_len:
            max_len = collatz_len_i
            result = i
    return result




def collatz_sequence_len(n: int) -> int:
    """
    Compute len of Collatz sequence.

    - O(1) space-complexity
    """
    result = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        result += 1
    return result


if __name__ == '__main__':
    print(f'Problem 14 solution: {problem_014()}')
