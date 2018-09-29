### COPIED ### VERIFIED
def longest_alternating_sequence(array):
    # create memo. There are two rows of length of array
    # Row 0 is for alternating sequence ending at a high
    # Row 1 is for alternating sequence ending at a low.
    # Initialize all to 1, because every element forms a sequence by itself.
    memo = [[1 for _ in range(len(array) + 1)] for _ in (0, 1)]

    for i in range(2, len(array) + 1):
        for j in range(1, i):
            if array[i-1] < array[j-1]: # array[i-1] is less. So this is a sequence ending at a low.
                # add this to memo[0][j], which was a sequence ending at high.
                memo[1][i] = max(memo[1][i], 1 + memo[0][j])
            if array[j-1] < array[i-1]:
                memo[0][i] = max(memo[0][i], 1 + memo[1][j])

    n = len(array)
    return max(memo[0][n], memo[1][n])


array = [1, 2, 5, 3, 2, 1]
print(longest_alternating_sequence(array))

