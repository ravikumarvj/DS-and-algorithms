#### COPIED ####
"""
Given two sorted arrays A and B of size m and n of distinct elements. Given a value x.
The problem is to count all pairs from both arrays whose sum is equal to x.

Method 1: Use two loops. For each element in A, go through B and find. O(n^2)
Method 2: Since it is sorted arrays, going through B can be done using binary search.
For each element in smaller array, use binary search for larger array.  O(mlogn), where n > m
Method 3: Use hashing. Put all the elements of smaller array in to hash.
For each element in larger array, check for (x-array[i]) in the hash-table.
O(m + n) with O(m) space complexity, where m , n
Method 4: 2sum as given below. O(m+n)
"""

def twosum_twoarray(array1, array2, X):
    i = 0
    j = len(array2) - 1

    while i < len(array1) and j >= 0:
        s = array1[i] + array2[j]
        if s == X:
            print(array1[i], array2[j])
            i += 1
            j -= 1
        elif s < X:
            i += 1
        else:
            j -= 1

    return

if __name__ == '__main__':
    array1 = [1, 3, 5, 7, 9, 10, 11]
    array2 = [2, 3, 4, 5, 6, 8, 11]
    X = 20
    twosum_twoarray(array1, array2, X)