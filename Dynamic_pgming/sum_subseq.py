#### COPIED ####  VERIFIED

from collections import defaultdict

def find_subsequence_non_neg(array, i, s, memo, items):
    if s == 0:
        return True
    if i == 0:
        return False

    if i in memo and s in memo[i]:
        return memo[i][s]

    # SUM(i, s) = SUM(i - 1, s) or SUM(i - 1, s - array[i])
    excl = find_subsequence_non_neg(array, i-1, s, memo, items)
    if excl:
        memo[i][s] = True
        return True  # If excl is find, no need to find incl

    if array[i-1] <= s:
        incl = find_subsequence_non_neg(array, i-1, s-array[i-1], memo, items)  # array is 0 based indexing
        if incl:
            items[i][s] = array[i-1]
            memo[i][s] = True
            return True

    memo[i][s] = False
    return False

def find_subsequnce_non_neg_bup(array, N, S):
    memo = [[0 for j in range(S + 1)] for i in range(N + 1)]
    for i in range(N + 1):
        memo[i][0] = True

    for s in range(S + 1):
        memo[0][s] = False

    for i in range(1, N + 1):
        for s in range(1, S + 1):
            excl = memo[i-1][s]
            incl = False
            if s >= array[i-1]:
                incl = memo[i-1][s-array[i-1]]
            memo[i][s] = excl or incl
    return memo[N][S]

# Changed flag is needed because, the initial S passed can be 0
def find_subsequence(array, i, s, changed, memo, elems): # first round, pass changed as False
    if s == 0 and changed:  # Should come before i==0 check so as to include array[0] as the solution
        return True         # Ex: array is [-4, 5] and s = -4

    if i == 0:
        return False
    if i in memo and s in memo[i]:
        return memo[i][s]

    ret = find_subsequence(array, i-1, s-array[i-1], True, memo, elems) # True as s is changed
    if ret:
        elems[i][s] = array[i-1]

    if ret is False:
        ret = find_subsequence(array, i-1, s, changed, memo, elems)
    memo[i][s] = ret

    return ret


def print_mems(elems, array, s):
    n = len(array)
    for i in range(n, 0, -1):
        if s in elems[i]:
            print(elems[i][s], end=' ')
            s -= elems[i][s]

    print()


def find_subarray(array, s):  # sliding window. No extra space needed.
    start = 0
    end = 0
    temp = 0

    while end < len(array):
        temp += array[end]
        end += 1

        while temp > s:
            temp -= array[start]
            start += 1

        if temp == s:
            return array[start:end]
    return None


def find_subarray_neg(array, s):
    start = 0
    hashtable = dict() # use hashtable to store previous sums
    curr_sum = 0

    hashtable[0] = -1
    while start < len(array):
        curr_sum += array[start]
        if curr_sum - s in hashtable:
            print(array[hashtable[curr_sum - s] + 1:start+1])
            return True
        hashtable[curr_sum] = start
        start += 1

    return False


from collections import defaultdict
def print_all_sub_array_neg(array, s):
    start = 0
    hashtable = defaultdict(list)
    curr_sum = 0

    hashtable[0] = [0]
    while start < len(array):
        curr_sum += array[start]
        if curr_sum - s in hashtable:  # curr_sum - s and not the other way around
            for index in hashtable[curr_sum - s]:
                print(array[index:start + 1])
        hashtable[curr_sum].append(start + 1)
        start += 1

    print(hashtable)
    return

# Cannot do bup easily as the S can be positive or negative or 0
# additionally S can vary from S-sum(array) to S+sum(array)
def find_subseq_bup(array, S):
    pass

"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
def divide_set(set):
    total = sum(set)
    if total % 2:
        return False
    find_sum = total//2

    memo = defaultdict(dict)
    elems = defaultdict(dict)

    return find_subsequence(set, len(set), find_sum, False, memo, elems)




if __name__ == '__main__':
    array = [4, 5, 6, 3, 12, 8, 2]
    s = 9
    # print(find_subarray(array, s))
    # print('***')
    array = [-2, 4, -6, 2, 8, -4, 6, -4, -12, 4]
    print(find_subarray_neg(array, 4))
    print_all_sub_array_neg(array, 4)
    print('***')
    array = [4, 5, 6, 3, 12, 8, 2]
    memo = defaultdict(dict)
    items = defaultdict(dict)
    s = 41
    # print(find_subsequence_non_neg(array, len(array), s, memo, items))
    # print_mems(items, array, s)
    # print(find_subsequnce_non_neg_bup(array, len(array), s))
    print('^^^^^^^^^^^')
    array = [-4, 3, -2, 5, 6, -3, 8, -7]
    memo = defaultdict(dict)
    elems = defaultdict(dict)
    S = 11
    # print(find_subsequence(array, len(array), S, False, memo, elems))
    # print(elems)
    # print_mems(elems, array, S)
    # set = [2, 2, 2, 2, 4, 1, 1, 1]
    # print(divide_set(set))