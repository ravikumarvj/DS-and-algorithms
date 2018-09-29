#### COPIED ####  VERIFIED
# Bottom-Up
def fibo(n):
    if n <= 0:
        return

    n1, n2 = 0, 1
    for i in range(n - 1):
        n2, n1 = n1 + n2, n2

    return n2


if __name__ == '__main__':
    for i in range(1, 10):
        print(fibo(i))
