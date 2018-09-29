### COPIED ###  VERIFIED
def count_decode(string, memo):
    if memo[len(string)] != -1:
        return memo[len(string)]

    count = 0
    # Do from backwards.
    if int(string[-1]) != 0:  # 0 cannot stand alone as last character
        ret = count_decode(string[:-1], memo)  # avoid last character
        count += ret

    if 0 < int(string[-2]) <= 2 and int(string[-1]) <= 6:  # last two characters <= 26
        ret = count_decode(string[:-2], memo)
        count += ret
    memo[len(string)] = count
    return count


def count_decode_front(string, index, memo):
    if memo[len(string)] != -1:
        return memo[len(string)]

    #base cases
    if len(string) == index:
        return 1  # found a decoding( includes empty string)

    if int(string[index]) == 0:  # no possible decoding
        return 0

    count = count_decode_front(string, index + 1, memo)
    if index + 1 < len(string) and 0 < int(string[index]) <= 2 and int(string[index + 1]) <= 6:
        count += count_decode_front(string, index + 2, memo)

    memo[index] = count
    return count


def count_decode_mem(string):
    memo = [-1] * (len(string) + 1)  # memo is O(n)
    memo[0] = 1
    memo[1] = 1
    print(count_decode(string, memo))

    memo = [-1] * (len(string) + 1)  # memo is O(n)
    print(count_decode_front(string, 0, memo))


count_decode_mem('9110242032103410241012120121202121054204242034')
count_decode_mem('2121021')
count_decode_mem('253')