from utils import is_prime


def problem_003(n: int = 600851475143) -> int:
    """
    - O(sqrt(n)) time-complexity
    - O(1) space-complexity

    In a loop from sqrt(n) to 1 check if i is factor of n and i is a prime number
    """
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            if is_prime(i):
                return i
    return 0  # return 0 otherwise


if __name__ == '__main__':
    print(f'Problem 3 solution: {problem_003()}')
