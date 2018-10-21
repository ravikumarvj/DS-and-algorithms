### COPIED ###  VERIFIED

def selection_sort(array):
    if len(array) <= 1:
        return

    for i in range(0, len(array)):
        small_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[small_index]:
                small_index = j

        array[i], array[small_index] = array[small_index], array[i]

    return

if __name__ == '__main__':
    array = [8, 5, 7, 12, 4, 1, 8]
    selection_sort(array)
    print(array)