from typing import Dict


num2word = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sexteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',
    1000: 'one thousand',
}


def two_num_translate(n: int, num2word: Dict[int, str] = num2word) -> str:
    if n in num2word:
        translate = num2word[n]
    else:
        first_num = n // 10 * 10
        second_num = n % 10
        translate = f'{num2word[first_num]}-{num2word[second_num]}'
    return translate


def three_num_translate(n: int, num2word: Dict[int, str] = num2word) -> str:
    if n in num2word:
        translate = num2word[n]
    else:
        first_num = n // 100 * 100
        second_and_third_num = n % 100
        translate = f'{num2word[first_num]} and {two_num_translate(second_and_third_num)}'
    return translate


def convert_num2word(n: int, num2word: Dict[int, str] = num2word) -> str:
    if len(str(n)) == 2:
        result = two_num_translate(n, num2word)
    elif len(str(n)) == 3:
        result = three_num_translate(n, num2word)
    else:
        result = num2word[n]
    return result


def drop_spaces_or_hyphens(word: str) -> str:
    return word.replace(' ', '').replace('-', '')


def problem_017(upper_bound: int = 1000, num2word: Dict[int, str] = num2word) -> int:
    """
    Solution using num2word mapping.
    """
    result = 0
    for n in range(1, upper_bound + 1):
        result += len(
            drop_spaces_or_hyphens(
                convert_num2word(n, num2word),
            ),
        )
    return result


if __name__ == '__main__':
    print(f'Problem 17 solution: {problem_017()}')
