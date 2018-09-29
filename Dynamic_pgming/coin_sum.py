#### COPIED #### VERIFIED

def coin_sum(coins, m, memo, selected):
    if m == 0:
        return 0

    # Momoization
    if memo[m] > 0:
        return memo[m]

    minim = m  # Keep minimum as m (made up of m 1 rupee coins)
    for cn in coins:
        if cn <= m:  # coin value <= money
            ret_val = coin_sum(coins, m-cn, memo, selected)
            minim = minim if minim < ret_val else ret_val
            if minim == ret_val:  # if current coin is selected, update selected array
                selected[m] = cn

    memo[m] = minim + 1  # Dont forget + 1
    return memo[m]

def print_selected(selected, m):
    while m > 0:
        print(selected[m], end=' ')
        m -= selected[m]
    print()


def coin_sum_bup(coins, m):
    memo = [m] * (m + 1)  # initialize as m, for ease of comparison
    memo[0] = 0

    for i in range(1, m+1):
        for cn in coins:
            if cn <= m:
                memo[i] = min(memo[i], memo[i-cn] + 1)

    return memo[m]


# Wrong code as it will print all the permutations. For example, if total is 3
# and coins are (1, 2), it will print, 3 [(1, 1, 1), (2, 1), (1, 2)]
def ways_of_making_sum_bup(total, coins):
    memo = [0] * (total + 1)

    for co in coins:
        if co <= total:
            memo[co] = 1

    for i in range(1, total + 1):
        count = 0
        for co in coins:
            if i - co > 0:
                count += memo[i - co]
        memo[i] += count  # +=

    return memo[total]


# Ways(total, coins, n) =
#     Ways(total - coins[n], coins, n)  # include coin[n]
#     +  Ways(total, coins, n-1) # exclude coin[n-1]
# This works compared to the above because we are maintaining specific order for coins
def ways_of_making_sum(total, coins):
    memo = [[0 for _ in range(len(coins) + 1)] for _ in range(total + 1)]

    # Making a sum of 0 can be done only in 1 ways
    for i in range(len(coins) + 1):
        memo[0][i] = 1

    for i in range(1, total + 1):
        for c in range(1, len(coins) + 1):
            #            include      + exlcude
            include, exclude = 0, 0
            if i-coins[c-1] >= 0:
                include = memo[i-coins[c-1]][c]  # i-coins[c-1]

            exclude = memo[i][c-1]  # c starts from 1. So, c-1 is always valid
            memo[i][c] = include + exclude

    return memo[total][len(coins)]


if __name__ == '__main__':
    coins = [1, 10, 19, 36]
    M = 123
    memo = [0] * (M + 1)
    selected = [0] * (M + 1)
    print(coin_sum(coins, M, memo, selected))
    print_selected(selected, M)
    print(coin_sum_bup(coins, M))

    coins = [1, 3, 5, 7]
    total = 8
    # print(ways_of_making_sum_bup(total, coins))
    print(ways_of_making_sum(total, coins))