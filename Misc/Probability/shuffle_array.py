#### COPIED ####
"""
Shuffle a given array
Given an array, write a program to generate a random permutation of array elements. This question is also asked as “shuffle a deck of cards” or “randomize a given array”.
"""

from random import random
from random import randint

def shuffle_array(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        a = randint(0, i)
        if a != i:
            arr[a], arr[i] = arr[i], arr[a]

    return arr


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(shuffle_array(array))
