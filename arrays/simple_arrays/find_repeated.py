### COPIED #### VERIFIED
"""
In the given array, there is one element that is repeated more than half. The remaining elements may be repeated or not.
Find the max repeated element.

For example: in [5, 4, 2, 5, 5, 4, 5, 5, 2], the result should be: 5
in [4, 4, 4, 4, 4, 4, 3, 3, 3, 3], result should be:4

We can use a hash table and find the solution in O(N) runtime and O(N) space.
We can also use the below method with O(N) space and O(N) runtime
"""

def find_repeated(arr):
    stk = [0] * len(arr)
    top = 0

    for i in arr:
        if top == 0:
            stk[top] = i
            top += 1
        else:
            if stk[top-1] == i: # check if the current top is same as 'i'
                stk[top] = i
                top += 1
            else:  # If different, just pop the top element
                top -= 1

    return stk[top - 1]


# same logic as above, but dont need stack. O(n)runtime, O(1)space
def find_repeated_boyer_moore(arr):
    count = 0
    temp_num = None

    for num in arr:
        if count == 0:
            temp_num = num
            count = 1
        else:
            if num == temp_num: # same number seen again
                count += 1
            else:
                count -= 1  # Count could become zero,
                # in which case a new temp_num will be selected in next iteration.

    # there is no guarantee that temp_num is repeated more than half times.
    # But if a number is repeated more than half, it is temp_num
    count = arr.count(temp_num)  # Re-verification
    if count <= len(arr)//2:
        return None
    return temp_num


if __name__ == '__main__':
    arr = [4, 3, 4, 3, 4, 5, 2, 4, 4]
    print(find_repeated(arr))
    print(find_repeated_boyer_moore(arr))