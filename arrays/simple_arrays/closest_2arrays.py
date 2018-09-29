### COPIED ###  VERIFIED
"""
Given two sorted arrays and a number x, find the pair (one from each array) whose sum is closest to x.
"""

def closest_numer(array1, array2, X):
    i = 0
    j = len(array2) - 1

    closest = (array1[i], array2[j])
    closeness = abs(X - (array1[i] + array2[j]))

    while i < len(array1) and j >= 0:
        s = array1[i] + array2[j]
        if abs(X-s) < closeness:
            closeness = abs(X-s)
            closest = (array1[i], array2[j])
        if s == X:
            break
        elif s < X:
            i += 1
        else:
            j -= 1

    print(closest)

if __name__ == '__main__':
    array1 = [2, 6, 10, 14, 18]
    array2 = [2, 5, 7, 9, 11, 15]
    X = 20
    closest_numer(array1, array2, X)
