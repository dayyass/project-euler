from utils import product, check_divisible


def problem_005(k: int = 20) -> int:
    """
    1) init number as product of all numbers from 1 to k;
    2) try to decrease the number (divide from k to 1) in a loop keeping the divisibility properties.

    - O(k) space-complexity
    - O(1) space-complexity
    """
    divisors = range(1, k + 1)
    num = product(divisors)  # take as initial number product of all numbers from 1 to k
    for i in range(k, 1, -1):
        if check_divisible(num // i, divisors):  # try to decrease the number keeping the divisibility properties
            num //= i
    return num


if __name__ == '__main__':
    print(f'Problem 5 solution: {problem_005()}')
