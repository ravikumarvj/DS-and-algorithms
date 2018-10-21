#### COPIED #### VERIFIED
def find_duplicate(array):
    xor_val = 0
    for i in array:
        xor_val ^= i

    return xor_val


def find_duplicate_two(array):
    axorb = 0
    for i in array:
        axorb ^= i

    xor_mask = axorb ^ (axorb - 1)
    a, b = 0, 0

    for i in array:
        if i & xor_mask:
            a ^= i
        else:
            b ^= i

    return (a, b)

array = [4, 3, 6, 2, 4, 2, 3, 4, 3, 3]

print(find_duplicate_two(array))