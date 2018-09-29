
### COPIED ###  VERIFIED

def lcs(a, b, i, j, memo):
    if i == 0 or j == 0:
        return 0

    if i in memo and j in memo[i]:
        return memo[i][j]

    if a[i-1] == b[j-1]:
        memo[i][j] = 1 + lcs(a, b, i-1, j-1, memo)
    else:
        first = lcs(a, b, i-1, j, memo)
        second = lcs(a, b, i, j-1, memo)
        memo[i][j] = max(first, second)

    return memo[i][j]


def print_incl_mem(a, b, incl):
    i = len(a)
    j = len(b)
    print('Longest common sequence is:', end = ' ')
    res = []

    while i > 0 and j > 0:
        # a[i-1] == b[j-1] check is mandatory because, if they are not matching,
        # the value would have come from i-1 or j-1
        if a[i-1] == b[j-1] and incl[i][j] == incl[i-1][j-1] + 1:
            res.append(a[i-1])
            i -= 1
            j -= 1
        elif incl[i][j] == incl[i-1][j]:
            i -= 1
        else:
            j -= 1
    print(res[::-1])
    return res[::-1]


def lcs_bup(a, b):
    M = len(a)
    N = len(b)

    memo = [[0 for i in range(N + 1)] for j in range(M + 1)]
    # We need memo[i][0] = 0 and memo[0][j] = 0
    # And by initialization, this is true

    for i in range(1, M+1):
        for j in range(1, N+1):
            if a[i-1] == b[j-1]:
                memo[i][j] = first = memo[i-1][j-1] + 1
            else:
                first = memo[i-1][j]
                second = memo[i][j-1]
                memo[i][j] = max(first, second)

    print_incl_mem(a, b, memo)
    return memo[M][N]


def diff_utility(a, b):
    memo = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    lcs(a, b, len(a), len(b), memo)
    seq = print_incl_mem(a, b, memo)
    print(seq)

    i = 0
    j = 0
    for c in seq:
        while c != a[i]:
            print('-', a[i], sep = '', end = ' ')
            i += 1
        while c != b[j]:
            print('+', b[j], sep='', end=' ')
            j += 1
        # at this point, c == a[i] and b[j]
        print(c, end=' ')
        i += 1
        j += 1

    print()


if __name__ == '__main__':
    a = 'abcbdab'
    b = 'bdcab'

    # memo = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    # print(lcs(a, b, len(a), len(b), memo))
    # print_incl_mem(a, b, memo)
    # print_incl_mem(a, b, memo)
    # print(lcs_bup(a, b))
    # diff_utility(a, b)

