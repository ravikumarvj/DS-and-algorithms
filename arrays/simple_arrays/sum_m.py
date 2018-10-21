### COPIED ###   VERIFIED
"""
Find 2 numbers in a sorted array that sum to M
Given a sorted array and a number M, find two numbers in sorted array whose sum equals to M.
"""
from collections import defaultdict


def find_pair_sum(array, num):  # Copied
    if len(array) < 2:
        return None, None

    front = 0
    back = len(array) - 1

    while front < back:
        temp = array[front] + array[back]
        if temp == num:
            return array[front], array[back]
        if temp < num:
            front += 1
        else:
            back -= 1

    return None, None


def find_pair_sum_all(array, num):  # Copied
    if len(array) < 2:
        print(None, None)

    front = 0
    back = len(array) - 1
    printed = False
    while front < back:
        temp = array[front] + array[back]
        if temp == num:
            print(array[front], array[back])
            printed = True
            front += 1
            back -= 1
        elif temp < num:
            front += 1
        else:
            back -= 1

    if printed is False:
        print(None, None)

    return


def find_pair_sum_hash(array, num):  # Copied
    st = set()

    for i in array:
        temp = num - i
        if temp in st:
            return temp, i
        st.add(i)  # Add only after checking. otherwise if num/2 is there in array, you may get wrond result as num/2, num/2
    return None, None


def find_pair_sum_hash_all(array, num):  # Copied
    # st = set() Cant use set because there could be duplicate elements
    dt = defaultdict(int)

    for i in array:
        temp = num - i
        if temp in dt:
            print(temp, i)
            dt[temp] -= 1
            if dt[temp] == 0:
                del dt[temp]
        else:
            dt[i] += 1


if __name__ == '__main__':
    array = (2, 6, 11, 25, 25, 30, 35, 35, 35, 40, 45, 45, 55)
    a, b = find_pair_sum(array, 70)
    print(a, b)
    a, b = find_pair_sum_hash(array, 70)
    print(a, b)
    print('-' * 10)
    find_pair_sum_all(array, 70)
    print('-' * 10)
    find_pair_sum_hash_all(array, 70)