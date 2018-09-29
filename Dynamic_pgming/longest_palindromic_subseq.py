### COPIED ###  VERIFIED
"""
Find palindrome (str, 0, len(str)-1)

palindrome(str, i, j) = {
                        if str[i] == str[j]: 2+palindrome(str, i+1, j-1)
                        else:
                            max(palindrome(str, i+1, j), palindrome(str, i, j-1)
"""



def l_palind_subseq(str, i, j, memo):  # i and j inclusive
    if i > j:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]

    if i == j:  # same character
        return 1

    if str[i] == str[j]:
        memo[i][j] = 2 + l_palind_subseq(str, i+1, j-1, memo)
    else:
        memo[i][j] = max(l_palind_subseq(str, i+1, j, memo),
                         l_palind_subseq(str, i, j-1, memo))
    return memo[i][j]

def print_seq(str, memo):
    i = 0
    j = len(str) - 1
    ret = []
    odd = False

    while i <= j:
        if str[i] == str[j]:
            ret.append(str[i])
            if i== j:
                odd = True
            i += 1
            j -= 1
        elif memo[i][j-1] == memo[i][j]:
            j -= 1
        else:
            i += 1

    # while reversing, dont give, -1 in the middle. when given, it is giving null array as -1
    # is being interpretted as end of array
    print('ravi'[3:-1:-1])
    if odd and len(ret) - 1:
        ret.extend(ret[len(ret)-2::-1])
    else:
        ret.extend(ret[len(ret)-1::-1])
    print(ret)


def longest_palindromic_subseq(str):
    memo = [[-1 for col in range(len(str))] for row in range(len(str))]
    ret = l_palind_subseq(str, 0, len(str)-1, memo)
    print_seq(str, memo)
    return ret


if __name__ == '__main__':
    string = 'mansalm'
    print(longest_palindromic_subseq(string))