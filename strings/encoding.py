#### COPIED ### VERIFIED
"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def run_length_encoding(string):
    ret = []
    count = 1
    if len(string) <  0:
        return ''

    char = string[0]
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            ret.append(str(count))
            ret.append(char)
            count = 1
            char = string[i]


    ret.append(str(count))
    ret.append(char)

    return ''.join(ret)

def run_length_decoding(string):
    l = list(string)
    ret = []

    for i in range(0, len(string), 2):
        ret.append(int(string[i]) * string[i+1])

    return ''.join(ret)


if __name__ == '__main__':
    encode = run_length_encoding('AABBBACCDDDAAAABB')
    print(encode)
    decode = run_length_decoding(encode)
    print(decode)