### COPIED ###

def next_larger(num):   # 4 2 3 8 6 2
    l = list(str(num))

    for i in range(len(l) - 2, -1, -1):
        if l[i + 1] > l[i]:
            for j in range(i+1, len(l)):
                m = '9'
                if m >= l[j] > l[i]:  # character comparison. Should be OK as we have only digits
                    sw = j
                    m = l[j]
            l[i], l[sw] = l[sw], l[i]   # should be outside for loop
            l[i + 1:] = sorted(l[i+1: ])
            break
    else:
        print('No larger element')
        return

    print(int(''.join(l)))   # int


def next_smaller(num):  # 4 2 3 8 6 2
    l = list(str(num))

    for i in range(len(l) - 2, -1, -1):
        if l[i+1] < l[i]:
            for j in range(i+1, len(l)):
                m = '0'
                print(l[i], l[j], m)
                if m <= l[j] < l[i]:
                    sw = j
                    m = l[j]
            l[i], l[sw] = l[sw], l[i]
            l[i+1:] = sorted(l[i+1:], reverse=True)
            break
    else:
        print('no smaller number')
        return

    print(int(''.join(l)))


def get_second_largest(num): # 4 2 3 8 6 2
    l = list(str(num))
    l.sort(reverse=True)  # ''.join(l.sort(reverse=True)) will give error as ''.join() will take return value of l.sort(), which is None

    print('largest = ', ''.join(l))
    for i in range(len(l) - 1, 0, -1):
        if l[i] != l[i-1]:
            l[i-1], l[i] = l[i], l[i-1]
            break
    print('second largest = ', ''.join(l))


if __name__ == '__main__':
    num = 423028
    next_larger(num)
    get_second_largest(num)
    next_smaller(num)