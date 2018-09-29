def zerosum_subarray(array):
    s = set()

    s.add(0)
    sum = 0

    for num in array:
        sum += num

        print(sum)
        if sum in s:
            return True
        else:
            s.add(sum)

    return False

def print_all_zero_sum(array):
    s = dict()
    s[0] = -1

    sum = 0

    for index, num in enumerate(array):
        sum += num
        if sum in s:
            print(array[s[sum]+1: index + 1])
        s[sum] = index


if __name__ == '__main__':
    array = [4, -4, 2, 0, -3, -1, 4]
    print(zerosum_subarray(array))
    print_all_zero_sum(array)