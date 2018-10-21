### COPIED #### VERIFIED
def longest_inc_subseq(array):
    N = len(array)
    # memo = [0] * (N + 1)
    # lis = [0] * (N + 1)
    prev = [-1] * (N + 1)
    memo = [1] * (N + 1)  # Consider each element as a start
    # for i in range(N):  # Consider each element as a start
    #    lis[i+1] = [array[i]]

    memo[1] = 1  # sub-seq of length 1 by array[0]
    # lis[1] = [array[0]]

    for i in range(2, N + 1):
        for j in range(1, i):
            if array[j-1] < array[i-1]:
                if memo[j] + 1 > memo[i]:
                    memo[i] = memo[j] + 1
                    prev[i] = j
                    # lis[i] = lis[j] + [array[i-1]]

        # With proper initialization of memo and lis, below code is not needed
        # if memo[i] == 0:  # No previous element less than this
        #     memo[i] = 1  # Better initialize memo and lis properly
        #     lis[i] = [array[i-1]]  # Consider this as new start

    largest = 1
    for i in range(1, N+1):
        if memo[i] > memo[largest]:
            largest = i

    print(memo, prev)
    print('Largest Sub sequence length is :', memo[largest])
    print('Sub sequence is :', end = ' ')
    temp = largest
    stk = []
    while temp != -1:
        stk.append(array[temp-1])
        temp = prev[temp]
    print(stk[::-1])

    return

if __name__ == '__main__':
    array = [2,3,5,8,6,7,1,2,3,24,5,6,10,41,15,31]
    longest_inc_subseq(array)