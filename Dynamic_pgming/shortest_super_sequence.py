### Copied ### VERIFIED
from longest_common_subseq import lcs, print_incl_mem

def super_seq(a, b):
    memo = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    lcs(a, b, len(a), len(b), memo)

    seq = print_incl_mem(a, b, memo)
    print(seq)

    ret = []
    l, i, j = 0, 0, 0
    while l < len(seq):
        while i < len(a) and a[i] != seq[l]:
            ret.append(a[i])
            i += 1
        while j < len(b) and b[j] != seq[l]:
            ret.append(b[j])
            j += 1
        ret.append(seq[l])
        l += 1
        i += 1
        j += 1

    ret.extend(a[i:])
    ret.extend(b[j:])

    print(a)
    print(b)
    print(''.join(ret))


# Print super sequence based on memo, a and b.
def print_sup_seq(a, b, memo):
    ret = []
    i = len(a)
    j = len(b)

    while i > 0 and j > 0:  # both i > 0 and j > 0.
        if a[i-1] == b[j-1]:  # characters are same. i-1/j-1
            ret.append(a[i-1]) # add it to result
            i -= 1
            j -= 1
        # else check if we need to decrease i or j.
        elif memo[i][j] == memo[i-1][j] + 1:
            ret.append(a[i-1])
            i -= 1
        else:
            ret.append(b[j-1])
            j -= 1
    ret.extend(a[:i])  # add whatever is left in a
    ret.extend(b[:j])  # add whatever is left in b
    print(''.join(ret[::-1]))  # reverse result.


def super_seq_len(a, b, a_in, b_in, memo):
    if memo[a_in][b_in] != 0:
        return memo[a_in][b_in]

    if a_in == 0:  # length of a is over. Add whaterver there in b to SCS
        memo[a_in][b_in] = b_in
    elif b_in == 0: # length of b is over. Add whaterver there in a to SCS
        memo[a_in][b_in] = a_in
    elif a[a_in - 1] == b[b_in - 1]:  # last characters same.
        memo[a_in][b_in] = 1 + super_seq_len(a, b, a_in - 1, b_in - 1, memo)
    else:  # last characters differ. Add one of those characters and SCS of remaining string
        memo[a_in][b_in] = 1 + min(super_seq_len(a, b, a_in - 1, b_in, memo),
                                   super_seq_len(a, b, a_in, b_in - 1, memo))

    return memo[a_in][b_in]


def super_seq_len_bup(a, b):
    memo = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a)):
        memo[i][0] = i # If b is of length 0
    for j in range(len(b)):
        memo[0][j] = j # if a is of length 0

    for i in range(1, len(a) + 1):  # Dont forget 1,
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                memo[i][j] = 1 + memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])

    print_sup_seq(a, b, memo)
    return memo[len(a)][len(b)]


a = 'abcbdab'
b = 'bdcab'
super_seq(a, b)
memo = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
print(super_seq_len(a, b, len(a), len(b), memo))
print_sup_seq(a, b, memo)
print(super_seq_len_bup(a, b))