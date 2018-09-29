##### COPIED #####  VERIFIED

"""
profit(p, k, i) = MAX(max( (p[i] - p[j]) + profit(p, j-1, k-1)) for j from i-1, 0), profit(p, k, i-1))

"""

def find_max_profit(price, k):
    memo = [[-1 for col in range(k+1)] for row in range(len(price))]
    return max_profit(price, len(price)-1, k, memo)


def max_profit(price, n, k, memo):
    profit = 0
    if memo[n][k] != -1:  # Memoiztion
        return memo[n][k]

    if k <= 0 or n <= 0:
        return 0

    # For a given k, profit = maximum of (sell at j,
    # what is bought at j and profit of subarray [0...j-1] for k-1 transactions)
    for j in range(n-1, -1, -1):
        if price[n] > price[j]:
            res = price[n] - price[j] + max_profit(price, j-1, k-1, memo)
            profit = max(profit, res)

    # now consider the possibility of making no transaction at price n.
    memo[n][k] = max(profit, max_profit(price, n-1, k, memo))
    return memo[n][k]


if __name__ == '__main__':
    price = [90, 80, 70, 60, 50]
    print(find_max_profit(price, 1))
