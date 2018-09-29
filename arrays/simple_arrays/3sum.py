### COPIED ###  VERIFIED
"""
Determine if any 3 integers in an array sum to 0.
For example, for array [4, 3, -1, 2, -2, 10], the function should return true since 3 + (-1) + (-2) = 0. To make things simple, each number can be used at most once.
"""


def find_3sum(array, num):  # Copied
    array.sort()

    for i in range(len(array) - 2):
        a = array[i]
        rest = num - a

        start = i + 1
        end = len(array) - 1

        while start < end:
            b, c = array[start], array[end]
            sm = b + c

            if rest == sm:
                print(a, b, c)
                return
            elif sm < rest:
                start += 1
            else:
                end -= 1

    print('None found')


def find_3sum_close (array, num):  # Copied
    array.sort()

    max_close = abs(num - (array[0] + array[1] + array[2]))
    a, b, c = array[0], array[1], array[2]

    for i in range(len(array) - 2):
        temp = num - array[i]

        start = i + 1
        end = len(array) - 1

        while start < end:
            two = array[start] + array[end]
            if two == temp:
                print(array[i], array[start], array[end])  # Nothing more close
                return
            else:
                if abs(num - (two + array[i])) < max_close:
                    max_close = abs(num - (two + array[i]))
                    a, b, c = array[i], array[start], array[end]
                if two < temp:
                    start += 1
                else:
                    end -= 1

    print(max_close, a, b, c)


def find_3sum_repeat(array, num):  # Copied
    array.sort()

    for i in range(len(array)):
        a = array[i]
        rest = num - a

        start = i  # start from the same i
        end = len(array) - 1

        while start <= end:  # start can be end
            b = array[start]
            c = array[end]
            sm = b + c

            if sm == rest:
                print(a, b, c)
                return

            if sm < rest:
                start += 1
            else:
                end -= 1

    print('None found')
    return


if __name__ == '__main__':
    array = [14, 1, -10, 2, 5, 10]
    find_3sum(array, 14)
    find_3sum_close(array, 8)
    find_3sum_repeat([2, 3, 7, 12, 20, 36, 40], 36)