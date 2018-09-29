#### COPIED ####  VERIFIED

def find_max_val(cakes, W, memo, items):
    if W == 0:
        return 0
    if memo[W] > 0:
        return memo[W]

    max_val = 0
    for w, v in cakes:
        if w <= W:
            inc_val = find_max_val(cakes, W-w, memo, items) + v
            max_val = max(max_val, inc_val)
            if max_val == inc_val:
                items[W] = w

    memo[W] = max_val
    return max_val


def print_items(items, W):
    while W > 0:
        if items[W] == 0:  # No items for exact weight W
            W -= 1
        else:
            print(items[W], end=' ')
            W -= items[W]
    print()

def find_max_val_bup(cakes, W):
    memo = [0]*(W+1)

    for i in range(1, W+1):
        for w, v in cakes:
            if w <= i:
                memo[i] = max(v + memo[i-w], memo[i])

    return memo[W]

if __name__ == '__main__':
    cake_tuples = [(5, 160), (3, 90), (2, 15), (8, 180), (4, 100)]
    capacity = 21

    memo = [0]*(capacity+1)
    items = [0]*(capacity+1)
    print(find_max_val(cake_tuples, capacity, memo, items))
    print_items(items, capacity)
    print(find_max_val_bup(cake_tuples, capacity))