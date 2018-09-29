## COPIED ## VERIFIED
def check_max_heap(array):
    N = len(array)
    # children i * 2 + 1 and i * 2 + 2
    for i in range(N//2): #  NBNBNB: N//2 exclusive
        print(i)
        left = i * 2 + 1
        right = i * 2 + 2

        large = i

        if array[left] > array[i]:
            return False
        if right < N and array[right] > array[i]:
            return False

    return True

if __name__ == '__main__':
    arr = [34, 18, 18, 14, 14, 1]
    print(check_max_heap(arr))
