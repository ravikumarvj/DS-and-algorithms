### COPIED #### VERIFIED
def find_sum(array, n, total, memo, elements):
    if total == 0:
        return True

    if n == 0:
        return False

    if n in memo and total in memo[n]:
        return memo[n][total]

    if array[n-1] == None:
        return find_sum(array, n-1, total, memo, elements)

    include = find_sum(array, n-1, total-array[n-1], memo, elements)
    if include:
        memo[n][total] = True
        elements[n][total] = array[n-1]
        return True

    exclude = find_sum(array, n-1, total, memo, elements)
    if exclude:
        memo[n][total] = True
        return True

    memo[n][total] = False
    return False


def print_nums(array, total, elements, res):
    n = len(array)

    result = []
    for i in range(n, 0, -1):
        if i in elements and total in elements[i]:
            result.append(elements[i][total])
            total = total - elements[i][total]
            array[i-1] = None
            if total == 0:
                break

    print(result)
    res.append(result)


from collections import defaultdict
def k_partition_print(array, k):
    total = sum(array)
    if total%k:
        print('No partition possible')
        return

    memo = defaultdict(dict)
    elements = defaultdict(dict)
    res = []
    for i in range(k):
        if find_sum(array, len(array), total//k, memo, elements):
            print_nums(array, total//k, elements, res)
            memo = defaultdict(dict)
            elements = defaultdict(dict)
        else:
            print(array)
            return False

    print(array) # array distroyed. Special case may be needed for leading zero
    print(res)
    return True

arr = [0, 2, 9, 5, 4, 8, 7, 0, 2, 2, 1, 4, 3, 4, 3, 9, 0]
k = 7
print(sum(arr))
print(k_partition_print((arr), k))