alphabet = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}


def problem_022(path: str = '../data/p022_names.txt') -> int:
    """
    Straightforward solution.
    """
    with open(path, mode='r') as fp:
        names = fp.read()
        names = names.replace('"', '').split(',')
        names.sort()

    result = 0
    for i, name in enumerate(names):
        position = i + 1
        alphabetical_value = sum(alphabet[letter] for letter in name)
        name_score = position * alphabetical_value
        result += name_score

    return result


if __name__ == '__main__':
    print(f'Problem 22 solution: {problem_022()}')
