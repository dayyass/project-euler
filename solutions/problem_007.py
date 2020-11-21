from utils import is_prime


def problem_007(n_prime: int = 10001) -> int:
    """
    Iterate over number, check if number is prime until reach desired prime number.

    - O(1) space-complexity
    """
    cnt = 0  # prime numbers counter
    num = 0  # current number
    while cnt != n_prime:
        num += 1
        if is_prime(num):
            cnt += 1
    return num


if __name__ == '__main__':
    print(f'Problem 7 solution: {problem_007()}')
