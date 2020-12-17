def problem_029(a_min: int = 2, a_max: int = 100, b_min: int = 2, b_max: int = 100) -> int:
    """
    Straightforward solution.
    """
    unique_powers = set()
    for a in range(a_min, a_max + 1):
        for b in range(b_min, b_max + 1):
            unique_powers.add(a**b)
    return len(unique_powers)


if __name__ == '__main__':
    print(f'Problem 29 solution: {problem_029()}')
