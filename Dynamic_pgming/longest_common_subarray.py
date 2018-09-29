##### COPIED ###### VERIFIED
def lcs(a, b):  # O(M*N*(min(M, N)). O(1) space
    M = len(a)
    N = len(b)
    i = 0
    maxim, start = 0, 0

    while i < M:
        j = 0
        while j < N:
            temp = i
            temp2 = j
            count = 0
            while temp2 < N and temp < M and a[temp] == b[temp2]:
                count += 1
                temp += 1
                temp2 += 1
            j += 1
            if count > maxim:
                start = i
                maxim = count
        i += 1

    print(maxim, a[start:start+maxim])


def lcs_bup(a, b):  # O(N^2), for both runtime and space
    M = len(a)
    N = len(b)

    lcs = ''
    max_len = 0

    # List of Lists as 2-d array, initialized to 0
    memo = [[0 for j in range(N + 1)] for i in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if a[i-1] == b[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
                if memo[i][j] > max_len:
                    max_len = memo[i][j]
                    lcs = a[i-max_len:i]  # a is 0-based array

    print(lcs, max_len)


if __name__ == '__main__':
    a = 'ababaaaabababababcbababcbaaabbbabbabababbbaaabbcbabaa'
    b = 'abbabcbbabbabababbbababbbaabbaababababababababca'

    lcs_bup(a, b)
    lcs(a, b)