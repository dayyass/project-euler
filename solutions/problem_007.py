from utils import prime_generator


def problem_007(n_prime: int = 10001) -> int:
    """
    Straightforward solution using prime_generator. Iterate over prime numbers up to n_prime.

    - O(1) space-complexity
    """
    for i, num in prime_generator():
        if i == n_prime:
            return num


if __name__ == '__main__':
    print(f'Problem 7 solution: {problem_007()}')
