### COPIED #### VERIFIED


def max_profit(arr):  # max profit from max 2 transactions
    if len(arr) < 2:
        return 0

    profit = [0] * len(arr)

    min_so_far = arr[0]
    # profit[i] contains profit that can be made on subarray arr[:i]
    for i in range(len(arr)):
        if arr[i] < min_so_far:
            min_so_far = arr[i]
        else:
            profit[i] = arr[i] - min_so_far
        profit[i] = max(profit[i-1], profit[i])

    # now do the same in reverse. For example, profit2[i] should contain profit
    # that can be made on sub-array arr[i:]. But we can reduce space by doing the
    # calculation on to the same profit array
    max_so_far = arr[-1]
    for i in range(len(arr)-2, 0, -1):  # Not including 1
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        else:
            # Profit of arr[:i]  i excluding + profit of arr[i:]
            profit[i] = profit[i-1] + max_so_far - arr[i]
        profit[i] = max(profit[i], profit[i+1])

    return profit[1]


price = [1, 15, 2, 32, 44, 100, 65, 23, 2, 23, 2, 110]
print ("Maximum profit is", max_profit(price))