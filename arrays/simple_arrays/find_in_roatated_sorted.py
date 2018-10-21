#### COPIED ###  VERIFIED

def find(array, num):  # search for num in array. Array is sorted, but rotated
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start)//2
        if array[mid] == num:
            return True

        if array[mid] < array[end]:  # Second half is sorted
            if array[mid] < num <= array[end]:  # check if num is in second half
                start = mid + 1
            else:
                end = mid - 1
        else:  # First half is sorted
            if array[start] <= num < array[mid]:  # Check id num is in first half
                end = mid - 1
            else:
                start = mid + 1

    return False

array = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
print(find(array, 0))
