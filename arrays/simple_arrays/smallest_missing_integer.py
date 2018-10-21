### COPIED ### VERIFIED

"""
    TODO: Write as Pattern
    Find the smallest positive number missing from an unsorted array
    You are given an unsorted array with both positive and negative elements.
    You have to find the smallest positive number missing from the array in
    O(n) time using constant extra space. You can modify the original array.

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2
"""

def segagrate(array):
    start = 0
    print(array)
    end = len(array) - 1
    while start <= end:
        if array[end] <= 0:
            end -= 1
        elif array[start] > 0:
            start += 1
        else:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
    return start

def find_missing_2(array):
    end = segagrate(array)
    print(array)
    for i in range(end):
        num = abs(array[i])
        if num <= end:
            array[num-1] = -(abs(array[num-1]))
    print(array)
    for i in range(end):
        if array[i] > 0:
            return i + 1

    return end + 1


"""
Find duplicates in O(n) time and O(1) extra space
Given an array of n elements which contains elements from 0 to n-1,
with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.

For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.
"""
# array = [2, 3, 0, 3, 2, 6, 0, 5, 6]  # Cant' get 2 and 6
def print_duplicates_1(array):  # WRONG SOLUTION, unless we add a pre-processing
    array = [x+1 for x in array]  # pre-processing
    duplicates = set()
    for i in range(len(array)):
        index = abs(array[i]) - 1

        if array[index] < 0:
            duplicates.add(index)
        else:
            array[index] = -array[index]

    return duplicates

def print_duplicates(array):
    # duplicates = set()
    for i in range(len(array)):
        index = array[i] % len(array)  # needed becasue we are putting -len(array), if array[i] = 0
        if len(array) <= array[index] < 2* len(array):
            # duplicates.add(index) # duplicates is not needed if we are adding len(array)
            print(index)
        else:
            array[index] = array[index] + len(array)
            if array[index] == 0:
                array[index] = len(array)

    # return duplicates


if __name__ == '__main__':
    array = [-2, 2, 1, 3, 2, -10, 234, 23, 69, 12, 4]
    array = [1, 1, 0, -1, -2]
    print(find_missing_2(array))

    # array = [2, 3, 0, 3, 2, 6, 0, 5, 6]
    # print_duplicates(array)
    # array = [2, 3, 0, 3, 2, 6, 0, 5, 6]
    # print(print_duplicates_1(array))
