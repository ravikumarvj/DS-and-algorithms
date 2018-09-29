### COPIED ###
from math import sqrt

def crossout(arr, prime, num):
    # Anything between prime and prime * prime, like prime-1 * prime etc should
    # be already crossed out, when we checked (prime - 1).
    # For example, if prime is 5, 4*5 is crossed out by 2, 3*5 by 3 etc.
    for x in range(prime*prime, num+1, prime):
        # in the loop, we step by prime. Because, anything in between will be
        # covered before
        if x%prime == 0:
            arr[x] = False

def make_list(arr):
    ret = list()
    for i in range(len(arr)):
        if arr[i] is True:
            ret.append(i)
    return ret


def sieve_of_eratosthenes(num):
    arr = [True for _ in range(num + 1)]
    arr[0] = False
    arr[1] = False

    for i in range(int(sqrt(num))):
        if arr[i] is True:
            crossout(arr, i, num)

    return make_list(arr)


if __name__ == '__main__':
    print(sieve_of_eratosthenes(50))  # Find all numbers below 50