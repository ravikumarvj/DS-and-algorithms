### COPIED ###
from random import randint

def print_k_from_stream(stream, k):
    reservoir = [0] * k
    count = 0

    for i in stream:
        if count < k:
            reservoir[count] = i
        else:
            n = randint(0, count)
            if n < k:
                reservoir[n] = i
        count += 1

    print(reservoir)


def print_one_from_stream(stream):
    num = None
    count = 0

    for i in stream:
        if num is None:
            num = i
        else:
            n = randint(0, count)
            if n == 0:
                num = i
        count += 1

    return num

if __name__ == '__main__':
    stream = range(100000)
    k = 50
    # print_k_from_stream(stream, k)
    count = 0
    while 1:
        count += 1
        ret = print_one_from_stream(stream)
        if 48000 < ret < 50000:
            break
    print(count, ret)
