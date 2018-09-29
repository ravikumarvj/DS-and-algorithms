##### COPIED ####  VERIFIED

from collections import defaultdict

def knap_sack_r(value, weight, i, w, memo, items):
    if i == -1 or w == 0:  # i means ith index. so, 0 items will be index -1
        return 0
    # Memoization
    if i in memo and w in memo[i]:
        return memo[i][w]

    excl = knap_sack_r(value, weight, i-1, w, memo, items)
    incl = 0
    if weight[i] <= w: # item 'i' can be included, if it's weight is <= w
        incl = knap_sack_r(value, weight, i-1, w-weight[i], memo, items) + value[i]

    memo[i][w] = max(excl, incl)  # Works because of defaultdict

    items[i][w] = -1
    if incl > excl:  # If i is included for (i, w), update items
        items[i][w] = i

    return memo[i][w]

# Value, is a list with item values, while weigh is list with item weights
# items is a dictionary used pto print items included
def knap_sack(value, weight, MAX_WEIGHT, items):
    memo = defaultdict(dict)
    return knap_sack_r(value, weight, len(value) - 1, MAX_WEIGHT, memo, items)

def print_items(items, w, weight, value):
    i = len(weight) - 1
    while w > 0 and i >= 0:
        if items[i][w] == -1:  # Item not included, check previous item
            i -= 1
        else:
            print(value[items[i][w]], end = ' ')
            w -= weight[items[i][w]]  # decrease weight
            i = i-1                   # decrease item
    print('')


# Iterative solution
def knapsack_bup(value, weight, mw):
    # In recursive method, all of i* w may not be filled in and hence we can have dictionary.
    # For bottup up, we need a complete i*w matrix unlike recursive method. So we use list of lists
    vals = [[0 for w in range((mw + 1))] for i in range(len(value) + 1)]
    n = len(value)

    # vals[0][w] and vals[i][0] is initialized to 0, as required
    # For each i (1..n) see if it needs to be included
    for i in range(1, n+1):
        for w in range(1, mw+1):
            excl = vals[i-1][w]  # Value excluding i
            incl = 0
            if weight[i-1] <= w:
                # value and weight is passed in 0 based index, hence i-1
                incl = vals[i-1][w-weight[i-1]] + value[i-1]
            vals[i][w] = max(incl, excl)

    return vals[n][mw]



if __name__ == '__main__':
    MAX_WEIGHT = 15
    value =  [30, 80, 43, 66, 18, 50, 23]
    weight = [2,  14, 9,  7,  4,  8,  3]

    items = defaultdict(dict)
    print(knap_sack(value, weight, MAX_WEIGHT, items))
    print(items)
    print_items(items, MAX_WEIGHT, weight, value)
    print(knapsack_bup(value, weight, MAX_WEIGHT))