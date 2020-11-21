from utils import is_palindromic


def problem_004(n_digits: int = 3):
    """
    In a loop from sqrt(n) to 1 check if i is factor of n and i is a prime number.

    - O(n^2) time-complexity
    - O(1) space-complexity
    """
    result = 0
    for i in range(10**n_digits - 1, 10**(n_digits - 1) - 1, -1):
        for j in range(10**n_digits - 1, 10**(n_digits - 1) - 1, -1):
            n = i * j
            if n < result:
                continue
            if is_palindromic(n):
                result = n
    return result


if __name__ == '__main__':
    print(f'Problem 4 solution: {problem_004()}')
