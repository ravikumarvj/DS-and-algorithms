"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def calculate_mapping(string):
    if len(string) == 0 or int(string[0]) == 0:
        return 0

    if len(string) == 1:
        return 1

    if len(string) == 2:
        ab = int(string)
        if ab == 10 or ab == 20:
            return 1
        elif 11 <= ab <= 26:
            return 2
        else:
            return 1


    a = int(string[0])
    b = int(string[1])
    ab = int(string[:2])
    count = 0

    if a == 0:
        return 0
    if b == 0:
        count += calculate_mapping(string[2:])
    else:
        count += calculate_mapping(string[1:])

        if ab <= 26:
            count += calculate_mapping(string[2:])

    return count

print(calculate_mapping('1010'))