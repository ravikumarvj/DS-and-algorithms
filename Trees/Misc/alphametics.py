from itertools import permutations
import re


def solve(p):
    p = p.upper()

    chars = re.findall(r'[A-Z]', p)
    unique_chars = set(chars)
    length = len(unique_chars)
    assert (length <= 10)

    first_chars = re.findall(r'\b[A-Z]', p)
    unique_first_chars = set(first_chars)

    sorted_string = ''.join(unique_first_chars) + ''.join(unique_chars - unique_first_chars)
    digits = [ord(d) for d in '0123456789']
    chars = [ord(c) for c in sorted_string]

    print(sorted_string)
    for i in permutations(digits, length):
        if ord('0') in i[:len(unique_first_chars)]:
            continue

        d = dict(zip(chars, i))
        if eval(p.translate(d)):
            print(p.translate(d))


if __name__ == '__main__':
    puzzle = "HAWAII + IDAHO + IOWA + OHIO == STATES"
    solve(puzzle)
