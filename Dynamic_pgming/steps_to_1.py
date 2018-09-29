#### COPIED ####  VERIFIED
def steps_to_1(num, path, memo):
    if num <= 0:
        raise Exception
    if num == 1:
        return 0

    if memo[num] > 0:
        return memo[num]

    a, b = num, num
    if num%3 == 0:
        a = steps_to_1(num//3, path, memo)
    if num%2 == 0:
        b = steps_to_1(num//2, path, memo)

    c = steps_to_1(num-1, path, memo)

    memo[num] = min(a, b, c) + 1
    if c < a and c < b:  # I initially put if a== b: assuming a == b == num. But a == b can be < num (for eg: num == 6)
        path[num] = 1
    else:
        path[num] = 3 if a < b else 2

    return memo[num]


def print_path(path, num):
    while num > 1:
        print(path[num], end = ' ')
        if path[num] == 1:
            num -= 1
        else:
            num //= path[num]
    print()


def steps_to_1_bottoms_up(num):
    if num <= 0:
        raise Exception

    if num == 1:
        return 0
    if num < 4:
        return 1

    memo = [0] * (num + 1)
    memo[1] = 0
    memo[2] = 1
    memo[3] = 1

    for i in range(4, num + 1):
        a = memo[i-1]
        b, c, = num, num
        if i%2 == 0:
            b = memo[i//2]
        if i%3 == 0:
            c = memo[i//3]

        memo[i] = min(a, b, c) + 1

    return memo[num]

if __name__ == '__main__':
    num = 997
    path = [0] * (num + 1)
    memo = [0] * (num + 1)  # Memoization
    print(steps_to_1(num, path, memo))
    print_path(path, num)

    print(steps_to_1_bottoms_up(num))