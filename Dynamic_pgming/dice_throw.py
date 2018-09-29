### COPIED ### VERIFIED

def count_throw(repeat, total, faces, memo, ret):
    if repeat == 0 and total == 0:
        # NB NB NB: with backtracing, it will work. but not with DP, because of memoization
        # With memoization, printing here wont give all results. We need to save the ret for each memo[i][j]
        # There is no easy way to print all the combinations
        # print(ret).
        return 1

    if repeat == 0 or total == 0:
        return 0

    if memo[repeat][total] != -1:
        return memo[repeat][total]

    count = 0
    for i in range(1, faces + 1):
        ret.append(i)
        count += count_throw(repeat - 1, total - i, faces, memo, ret)
        ret.pop()

    memo[repeat][total] = count
    return count


def count_throw_bup(repeat, total, faces):
    memo = [[0 for _ in range(total + 1)] for _ in range(repeat + 1)]

    memo[0][0] = 1
    for i in range(1, total + 1):
        memo[0][i] = 0

    for j in range(1, repeat + 1):
        memo[j][0] = 0

    for i in range(1, repeat + 1):
        for j in range(1, total + 1):
            for k in range(1, faces + 1):
                memo[i][j] += memo[i-1][j-k]

    return memo[repeat][total]

def count_num_throws(repeat, total, faces):
    memo = [[-1 for _ in range(total + 1)] for _ in range(repeat + 1)]
    ret = []
    return count_throw(repeat, total, faces, memo, ret)

print(count_num_throws(4, 15, 6))
print(count_throw_bup(4, 15, 6))