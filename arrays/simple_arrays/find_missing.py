#### COPIED ####  VERIFIED
"""
Given an array of length n, containing numbers from 1 to n,
except that one of the numbers is repeated and another is missing, find the missing number
"""

def find_missing(arr):
    n = len(arr)

    xor_val = 0
    for i in arr:
        xor_val ^= i
    for i in range(1, n+1): # 1...n
        xor_val ^= i

    # now, xor_val = missing ^ repeated
    one = 0
    two = 0

    for i in arr:
        if xor_val & i:
            one ^= i
        else:
            two ^= i
    for i in range(1, n+1):
        if xor_val & i:
            one ^= i
        else:
            two ^= i

    print(one, two)
    for i in arr:
        if one == i:
            print('missing = ', two)
            return
    print('missing = ', one)

if __name__ == '__main__':
    arr = [15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    find_missing(arr)