### COPIED ###  VERIFIED
"""
Given an array of numbers, partition it in to 3 subsets of equal sum
"""

def t_partition(array, n, first, second, third, memo):
    # all the sums are 0 and no more elements in array, we are done
    if n == 0 and first == 0 and second == 0 and third == 0:
        return True

    # all elements are done, but one or more partition-sum is not 0
    if n == 0:
        return False

    # Check if already done
    if (n, first, second, third) in memo:
        return memo[(n, first, second, third)]

    if first-array[n-1] >= 0:  # NBNBNB Can do only if all the numbers are all positive.
        res = t_partition(array, n-1, first-array[n-1], second, third, memo)
        if res:
            memo[(n, first, second, third)] = True
            return True

    if second - array[n - 1] >= 0:
        res = t_partition(array, n-1, first, second-array[n-1], third, memo)
        if res:
            memo[(n, first, second, third)] = True
            return True

    if third - array[n - 1] >= 0:
        res = t_partition(array, n-1, first, second, third-array[n-1], memo)
        if res:
            memo[(n, first, second, third)] = True
            return True

    memo[(n, first, second, third)] = False
    return False


def three_partition(array):
    total = sum(array)
    if total%3:  # if not divisible by 3, no partition is possible
        print('No partition possible')
        return

    memo = {}
    single = total//3
    # try to partition in to 3 subsets of sum total//3 each.
    return t_partition(array, len(array), single, single, single, memo)


def find_sum(array, n, total, memo, elements):
    if total == 0:
        return True

    if n == 0:
        return False

    if n in memo and total in memo[n]:
        return memo[n][total]

    if array[n-1] == None:  # this number was used in previous set
        return find_sum(array, n-1, total, memo, elements)

    include = find_sum(array, n-1, total-array[n-1], memo, elements)
    if include:
        memo[n][total] = True
        elements[n][total] = array[n-1]  # set elements to print the set
        return True

    exclude = find_sum(array, n-1, total, memo, elements)
    if exclude:
        # no setting of elements here as its excluded
        memo[n][total] = True
        return True

    memo[n][total] = False
    return False


def print_nums(array, total, elements, res):
    n = len(array)

    result = []
    for i in range(n, 0, -1):  # Do from last to first as done in find_sum()
        if i in elements and total in elements[i]:
            result.append(elements[i][total])
            total = total - elements[i][total]
            # set the corresponding number in array to None so that it wont be reused
            array[i-1] = None
            if total == 0:
                break

    print(result)
    res.append(result)


from collections import defaultdict
def three_partition_print(array):
    total = sum(array)
    if total%3:
        print('No partition possible')
        return

    memo = defaultdict(dict)
    elements = defaultdict(dict)
    res = []
    for i in range(3):  # loop 3 times and try to find a set of sum total/3 each time
        # NBNBNB. This will work only if we have positive numbers.
        # If negative number is there, it might un-necessarily go with an earlier partition
        # arr = [6, 2, 2, 2, 2, -2, 0], we might get first array as [2, 2, 2, -2]
        # Even adding a fixed constant to all numbers may not work. For example, even if we add 2 to
        # all numbers, we will add 7 * 2 = 14 to the total sum, which is not divisible by 3.
        if find_sum(array, len(array), total//3, memo, elements):
            print_nums(array, total//3, elements, res)  # add the numbers to result
            memo = defaultdict(dict)
            elements = defaultdict(dict)
        else:
            return False

    print(array) # array distroyed. Special case may be needed for leading zero
    return True

arr = [0, 6, 9, 5, 8, 7, 0, 2, 2, 1, 4, 3, 4, 3, 9, 0]
arr = [6, 3, 3, 3, 3]
print(sum(arr))
print(three_partition(arr))
print(three_partition_print(arr))