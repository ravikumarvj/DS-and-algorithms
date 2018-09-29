### COPIED ### VERIFIED

def find_max_profit_rec(array, i, memo, incl):
    if len(array) == i:
        return 0

    if memo[i] != -1:
        return memo[i]

    excl_profit = find_max_profit_rec(array, i + 1, memo, incl)
    incl_profit = array[i][2]

    temp = None
    for k in range(i+1, len(array)):
        # if array[k][0] >= array[i][1]:
        if array[i][0] <= array[k][0] < array[i][1]:
            continue

        incl_profit += find_max_profit_rec(array, k, memo, incl)
        temp = (i, k)
        break

    memo[i] = max(excl_profit, incl_profit)
    if memo[i] == excl_profit:
        incl[i] = None, i+1
    else:
        incl[i] = i, i
        if temp:
            incl[i] = temp

    return memo[i]


def print_save_2(save, array):
    print(save)
    i = 0
    while i < len(array):
        if save[i][0] == save[i][1]:  # same index. Means break out
            print(array[save[i][0]])
            break
        if save[i][0] is not None:
            print(array[save[i][0]], end = ' ')
        i = save[i][1]
    return


def find_max_profit(array):
    # going from start to end, sort on start time. Comparision are between this and subsequent elements
    array.sort(key=lambda x:x[0])  # Here, sort is based on start time.
    memo = [-1] * len(array)
    incl = [-1] * len(array)
    profit = find_max_profit_rec(array, 0, memo, incl)
    print(array)
    print_save_2(incl, array)
    print(profit)
    return max(profit, 0) # if profit is negative, return 0



def print_save(save, array):
    print(save)
    i = len(save) - 1
    while i >= 0:
        if save[i][0] == save[i][1]:  # same index. Means break out
            print(array[save[i][0]])
            break
        if save[i][0] is not None:
            print(array[save[i][0]], end = ' ')
        i = save[i][1]
    return


def find_max_profit_bup(array):
    # sort on finish. We compare this to previous ones.
    array.sort(key=lambda x:x[1])  # sort based in finish time

    memo = [0] * len(array)
    save = [0] * len(array)  # used to print the included element

    memo[0] = array[0][2]  # initialize memo for the first element
    # in save's tuple, first value will indicate if the current value is included in
    # the result or not. it will be equal to index, if included, else None. Second
    # value indicated the previous element in the result
    save[0] = (0, 0)

    print(array)
    for i in range(1, len(array)):
        memo[i] = max(array[i][2], memo[i-1])  # max of profit of element, and profit without this element
        if memo[i] == array[i][2]:
            save[i] = i, i # Only array[i] in result
        else:
            save[i] = None, i-1  # array[i] is not there. Got value from previous element

        for j in range(i-1, -1, -1):
            if array[i][0] >= array[j][1]:
                # update memo, if 'i' can be included with any other previous profit
                memo[i] = max(memo[i], memo[j] + array[i][2] )
                if memo[i] == memo[j] + array[i][2]:
                    save[i] = i, j  # i included, along with j
                break  # break out. No need to go any further down. Only one is enough        

    print_save(save, array)
    print(memo[len(array) - 1])



# tuple =  (start time, end time, profit)
array = [(1, 2, 20), (1, 4, 40), (3, 5, 30), (0, 6, 70), (5, 7, 30), (3, 8, 60), (5, 9, 50), (6, 10, 50), (8, 11, 40), (8, 12, 50), (2, 13, 150), (12, 14, 30)]
# array = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]

find_max_profit(array)
find_max_profit_bup(array)