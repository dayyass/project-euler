from utils import is_prime


def quadratic_n_primes(a: int, b:int) -> int:
    """
    Count quadratic primes for a and b params (n^2 + a*n + b).
    """
    n = 0
    quad = lambda x: x ** 2 + a * x + b
    while True:
        if not is_prime(quad(n)):
            break
        n += 1
    return n


def problem_027(a_min: int = -999, a_max: int = 999, b_min: int = -1000, b_max: int = 1000) -> int:
    """
    Straightforward solution. Iterate over all a and b params to find max number of quadratic primes.
    """
    n_primes_res, a_res, b_res = 0, 0, 0
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            n_primes = quadratic_n_primes(a=a, b=b)
            if n_primes > n_primes_res:
                n_primes_res, a_res, b_res = n_primes, a, b
    return a_res * b_res


if __name__ == '__main__':
    print(f'Problem 27 solution: {problem_027()}')
