from utils import is_pandigital


def find_upper_bound(n: int) -> int:
    """
    Helper function to find upper search bound.
    """
    return 10 ** (n // 2)


def problem_032(n: int = 9) -> int:
    """
    Collect all unique suitable numbers up to upper bound and sum them all.

    - O(n^2) time-complexity
    - O(1) space-complexity
    """
    unique_pandigital = set()
    upper_bound = find_upper_bound(n)
    for a in range(1, upper_bound):
        for b in range(1, upper_bound):
            prod = a * b
            concat = f'{a}{b}{prod}'
            if len(concat) != n:  # filter short/long multiplicand/multiplier/product identity
                continue
            if is_pandigital(int(concat)):
                unique_pandigital.add(prod)
    return sum(unique_pandigital)


if __name__ == '__main__':
    print(f'Problem 32 solution: {problem_032()}')
