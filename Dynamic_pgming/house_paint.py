#### COPIED ### VERIFIED
"""
MinCost(n, k) = Min(cost(n, j) + [MinCost(n-1, k), when n-1 is not painted with j) for k in 0 to k
"""

def _paint_house(n, k, cost, memo):
    # initialize the memo array for just one housel
    # memo contains cost of painting i'th house with kth colour
    for i in range(k):
        memo[0][i] = cost[0][i]

    for i in range(1, n):
        for j in range(k):
            memo[i][j] = cost[i][j] + min(memo[i-1][:j] + memo[i-1][j+1:])

    print(min(memo[n-1]))


def paint_house(n_houses, k_colours, cost):
    memo = [[0 for i in range(k_colours)] for j in range(n_houses)]
    return _paint_house(n_houses, k_colours, cost, memo)


if __name__ == '__main__':
    cost = [[3, 6, 5, 6, 8], [3, 6, 4, 5, 9], [4, 2, 9, 6, 3], [3, 3, 6, 5, 2], [6, 5, 5, 5, 2], [5, 4, 4, 4, 3]]
    paint_house(6, 5, cost)