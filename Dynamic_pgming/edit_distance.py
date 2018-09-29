#### COPIED ####  VERIFIED
"""
The edit distance between two strings refers to the minimum number of character insertions, deletions,
and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def find_edit_distance(start, target, memo):
    if memo[len(start)][len(target)] >= 0:
        return memo[len(start)][len(target)]

    if len(start) == 0:
        return len(target)  # This much to insert
    if len(target) == 0:
        return len(start)   # This much to delete

    if start[0] == target[0]:
        ret = find_edit_distance(start[1:], target[1:], memo)
    else:
        ret = 1 + min(find_edit_distance(start[1:], target, memo),      # delete start[0]
                      find_edit_distance(start[1:], target[1:], memo),  # substitute start[0] with target [0]
                      find_edit_distance(start, target[1:], memo))      # insert target[0] to the beginning of start

    memo[len(start)][len(target)] = ret
    return ret


def find_edit_distance_bup(start, target):
    # We dont need to maintain complete array.
    # We just need to have prev complete row and prev complete coloumn
    memo = [[-1 for i in range(len(target) + 1)] for j in range(len(start) + 1)]
    # memo have len(start) number of rows and len(target) number of columns

    memo[0][0] = 0
    for i in range(1, len(target) + 1):
        memo[0][i] = i  # target have i extra characters

    for i in range(1, len(start) + 1):
        memo[i][0] = i  # start have i extra characters

    for i in range(1, len(start) + 1):
        for j in range(1, len(target) + 1):
            if start[i-1] == target[j-1]:  # Dont forget the i-1 and j-1
                memo[i][j] = memo[i-1][j-1]
            else:
                # here, memo[i-i][j-1] == substitute
                ret1, ret2, ret3 = memo[i-1][j-1], memo[i-1][j], memo[i][j-1]
                memo[i][j] = 1 + min(ret1, ret2, ret3)

    return memo[len(start)][len(target)]

if __name__ == '__main__':
    start = 'sunday'
    target = 'saturday'
    memo = [[-1 for i in range(len(target) + 1)] for j in range(len(start) + 1)]
    print(find_edit_distance(start, target, memo))
    print(find_edit_distance_bup(start, target))