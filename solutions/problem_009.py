def problem_009(n: int = 1000) -> int:
    """
    Use loop over a with nested loop over b (express c = n - a - b).

    - O(n^2) time-complexity
    - O(1) space-complexity
    """
    for a in range(1, n // 2 + 1):
        for b in range(1, n // 2 + 1):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return 0


if __name__ == '__main__':
    print(f'Problem 9 solution: {problem_009()}')
