### COPIED ###  Verified

"""
I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:
•	The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
•	The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means:
 stock_prices[60] = 500


Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
For example:
stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.

A trade have to be definitely made. So we have to take care of loss as well.

"""

def get_total_profit_print_days(stock_prices):
    profit = 0
    solution = []

    profit = 0
    start = 0
    while start < len(stock_prices) - 1:
        # find the minimum starting at this point (such that next > this)
        while start < len(stock_prices) - 1 and stock_prices[start] >= stock_prices[start+1]:
            start += 1

        # at this point, either start = len(stock_prices) - 1 or stock_prices[next] > stock_prices[this]
        if start >= len(stock_prices) - 1:
            break  # no more solutions

        solution.append(start)  # Buy at this price
        start += 1

        # find local maximum.
        while start < len(stock_prices)-1 and stock_prices[start] < stock_prices[start+1]:
            start += 1

        # at this point, either start = last element or stock_prices[next] < stock_prices[this]
        solution.append(start)  # sell at this price
        profit += stock_prices[solution[-1]] - stock_prices[solution[-2]]
        start += 1  # consider next buying point

    print(solution)
    return profit


# Profit by any number of transactions
def get_total_profit(stock_prices):
    profit = 0
    min_val = stock_prices[0]

    for i in range(1, len(stock_prices) - 1):
        if stock_prices[i] < min_val:
            min_val = stock_prices[i]
        if stock_prices[i] > stock_prices[i+1]:
            temp = stock_prices[i] - min_val
            if temp > 0:
                profit += temp
            min_val = stock_prices[i+1]

    temp = stock_prices[-1] - min_val
    if temp > 0:
        profit += temp

    return profit


# profit by just one buy and one sale
def get_profit(stock_prices):
    if len(stock_prices) < 2:
        return None

    min_val = min(stock_prices[0], stock_prices[1])
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(2, len(stock_prices)):
        if stock_prices[i] - min_val > max_profit:
            max_profit = stock_prices[i] - min_val
        if stock_prices[i] < min_val:
            min_val = stock_prices[i]

    return max_profit


if __name__ == '__main__':
    array = [11, 10, 1, 8, 13, 11, 9, 20, 2, 1, 3, 4]

    print(get_profit(array))
    print(get_total_profit(array))
    print(get_total_profit_print_days(array))