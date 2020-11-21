def problem_015(n: int = 20) -> int:
    """
    Using dynamic programming from lower-right corner to upper-left corner.

    - O(n^2) time-complexity
    - O(n^2) space-complexity
    """
    array = [[1] * (n + 1)] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            array[i][j] = array[i-1][j] + array[i][j-1]
    return array[n][n]


if __name__ == '__main__':
    print(f'Problem 2 solution: {problem_015()}')
