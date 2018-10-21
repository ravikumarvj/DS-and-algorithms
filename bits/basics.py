### COPIED ###  VERIFIED

def get_bit(number, bit_no):  # Zero based bit numbering
    # Just doing & will clear rest of the bit.
    return (number & (1 << bit_no)) >> bit_no

def get_bit_one(number, bit_no):  # One based bit numbering
    return number & (1 << (bit_no) - 1) != 0

def set_bit(number, bit_no):  # Zero based bit numbering
    return number | (1 << bit_no)

def clear_bit(number, bit_no):
    and_num = ~(1 << bit_no)  # 0 at bit_no. Rest all 1's
    return number & and_num

def clear_bits_zero_to_bit_no(number, bit_no): # including bit_no
    and_num = ~0 << (bit_no + 1)
    return number & and_num

def clear_bits_top_to_bit_no(number, bit_no):
    and_num = (1 << bit_no) - 1
    return number & and_num

def toggle_bit(number, bit_no):
    xor_num = 1 << bit_no
    return number ^ xor_num

def swap_bits(number, p, q):
    pb = number & (1 << p)
    qb = number & (1 << q)

    if pb != qb:
        number = number ^ (1 << p)
        number = number ^ (1 << q)

    return number

def is_power_of_two(number):
    return (number & (number - 1)) == 0

def count_set_bits(number):
    count = 0
    while number:
        count += 1
        number &= (number - 1)

    return count

def if_odd(number):
    return number & 1 == 1

def if_even(number):
    return number & 1 == 0

def add_one(number):
    return -~number

def swap1(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap2(a, b):
    a = a ^ b   # a contains bit differences
    b = a ^ b   # xoring with b zeros out bit differences of b to give a
    a = a ^ b   # now, b is a. zoring with differences will give b
    return a, b

def rightmost_set_bit(number):
    # reset right most bit
    temp = (number & number-1)
    from math import log2

    temp = number ^ temp
    # temp now is power of 2

    return int(log2(temp))  # log return float

def rightmost_set_bit2(number):
    pos = 0
    while number & 1 == 0:
        pos += 1
        number >>= 1
    return pos

def rightmost_set_bit3(number):
    # reset right most bit
    temp = (number & number-1)

    temp = number ^ temp
    # temp now is power of 2

    map = {1:0, 2:1, 4:2, 8:3, 16:4, 32:5, 64:6, 128:7, 256:8, 512: 9, 1024:10, 2048:11, 4096:12}

    return map[temp]


def to_upper(c):
    return chr(ord(c) - ord('a') + ord('A'))

def convert_bits(number1, number2):
    temp = number1 ^ number2
    return count_set_bits(temp)

def check_palindrome(number):
    if number % 2 == 0:
        return False

    temp = number
    reverse = 0
    while temp:
        reverse = (reverse << 1) | (temp & 1)
        temp >>= 1

    return number == reverse

def reverse_number(number):
    # in python the number have infinite size. But here, we still check if it is 32-bit/64-bit
    import platform
    if platform.architecture()[0] == '64bit':
        loop = 32
    else:  # 32 bits
        loop = 32

    reverse = 0
    while number and loop > 0:
        reverse = (reverse << 1) | (number & 1)
        loop -=1
        number >>= 1

    return reverse


def reverse_number_alt(number):
    from math import log2

    reverse = 0
    prev_pos = 0
    while number:
        pos = int(log2(number & -number))  # position of rightmost set bit
        reverse = (reverse << (pos-prev_pos)) | 1
        prev_pos = pos
        number &= (number - 1)  # unset the rightmost bit position

    return reverse


def rightmost_set_bit(number):
    from math import log2
    return int(log2(number & -number))

def check_power_of_4(number):
    from math import log
    if float(int(log(number, 4))) == log(number, 4):
        print(True)
    else:
        print(False)

    if number & (number-1):
        return False
    if number % 3 == 1:
        print(True)
    else:
        print(False)


    count = -1
    num = number
    while num:
        count += 1
        num >>= 1

    if count%2 == 0:
        return True
    return False

def swap_n_bits(number, pos1, pos2, n):   # COPIED
    n_bits = (1 << n) - 1
    pos1_bits = (number >> pos1) & n_bits
    pos2_bits = (number >> pos2) & n_bits

    xor_bits = pos1_bits ^ pos2_bits  # a ^ (a ^ b) = b
    number = number ^ (xor_bits << pos2) ^ (xor_bits << pos1)  # a ^ 0 = a
    return number


def previous_and_next_power_of_two(number):
    temp = number
    while temp & (temp - 1):
        temp &= (temp - 1)

    print('previous: ', temp)

    temp = number - 1
    while temp & (temp - 1):
        temp &= (temp - 1)
    print('Next: ', temp << 1)

def add_two_binary_nums(a, b):
    print(a, b, a+b)
    total = 0
    carry = 0
    pos = 0

    import platform  # In python, negative numbers are of infinite length
    if platform.architecture()[0] == '64bit':
        loop = 64
    else:  # 32 bits
        loop = 32

    while (a or b or carry) and loop:  # Loop until a or b or carry exist for(32/64) times max
        sm = (a & 1) + (b & 1) + carry  # Dont forget (). + have precedence.
        if sm > 1:  # sm can be 0, 1, 2 or 3. 2 = 10, 3 = 11
            carry = sm // 2
            sm = sm % 2
        else:
            carry = 0

        total |= (sm << pos)  # Put the bit in correct position of total
        pos += 1
        a >>= 1  # >>=
        b >>= 1
        loop -= 1

    # given that python have infinite length integers, negative numbers total will be a positive number always
    # Even when you add -2 + 1 and get all leading 1's (-1), python will print it as positive number.
    return bin(total)

def two_odd_occuring_number(array):
    xor_val = 0
    for num in array:
        xor_val ^= num

    # xor_val = a^b, where a and b are odd occuring numbers
    from math import log2  # A bit in xor_val is set if they are having different vals in a and b
    pos = int(log2(xor_val & -xor_val)) # right most set bit position of xor_Val

    # Now, there are two disjoint sets of numbers in array such that
    # one set have its pos bit set and the other set don't have.
    # Each set have one number occuring odd number of times while rest all are even
    pos_map = 1 << pos
    a = 0
    b = 0
    for num in array:
        if num & pos_map == 0:
            a ^= num
        else:
            b ^= num
    print(a, b)

def swap_adjacent_bits(number):
    length = number.bit_length()
    length = length//4 + 1  # Handles negative number also
    mask1 = '0x' + 'A' * length
    mask2 = '0x' + '5' * length
    mask1 = int(mask1, 16)
    mask2 = int(mask2, 16)

    even = number & mask1
    odd  = number & mask2  # same as mask1 >> 1

    # if it was 'C', we could have the mask1 and mask2 of length 32 bit each
    # And we dont need this mechanism of getting whatever is left in number
    mask = (-1 << length * 4)  # take whatever is left in number

    number = (number & mask) | (even >> 1) | (odd << 1)
    return number

def find_missing_and_duplicate(array):
    length = len(array)  # range 1..length
    sum_range = sum(range(1, length + 1))
    a_minus_b = sum(array) - sum_range

    sum_2_range = sum([a*a for a in range(1, length + 1)])
    a2_minus_b2 = sum([a*a for a in array]) - sum_2_range

    a_plus_b = a2_minus_b2//a_minus_b

    a = (a_plus_b + a_minus_b)//2
    b = a_plus_b - a
    print(a, b)

    a_xor_b = 0
    for i in range (1, length + 1):
        a_xor_b ^= i
    for a in array:
        a_xor_b ^= a

    from math import log2
    pos = int(log2(a_xor_b & -a_xor_b))
    a = 0
    b = 0

    for i in range(1, length + 1):
        if i & (1 << pos):
            a = a^i
        else:
            b = b^i
    for num in array:
        if num & (1 << pos):
            a = a^num
        else:
            b = b^num
    print(a, b)

def replace_bits_at_position(number, bits, pos):
    length = bits.bit_length()
    mask = (1 << length) - 1
    existing = (number & (mask << pos)) >> pos  # Dont forget >> pos
    xor = bits ^ existing

    number ^= (xor << pos)
    return number


def subtract(a, b):
    return a + (~b + 1)

if __name__ == '__main__':
    a = 0b10110110101
    b = 0b110101101011

    print(bin(a))
    print(bin(b))

    # print(check_palindrome(0b1100110110011))

    a = 0b101101000
    # print(rightmost_set_bit(a))
    # print(rightmost_set_bit2(a))
    # print(rightmost_set_bit3(a))
    # print(check_power_of_4(1020))
    # print(bin(swap_n_bits(a, 0, 5, 3)))
    # previous_and_next_power_of_two(1020)

    # print(reverse_number(1010))

    # print(rightmost_set_bit(1))

    # print(reverse_number_alt(1010))
    # print(add_two_binary_nums(-10, -20))

    array = [5, 5, 19, 3, 3, 8, 4, 2, 8, 5, 2, 8, 4, 5]
    two_odd_occuring_number(array)
    # print(swap_adjacent_bits(381932474324232555664564576574624))
    # print(bin(b))
    # print(bin(replace_bits_at_position(b, 0b111001, 3)))
    array = [1, 2, 3, 4, 5, 1]
    find_missing_and_duplicate(array)

    print(subtract(-5, 9))