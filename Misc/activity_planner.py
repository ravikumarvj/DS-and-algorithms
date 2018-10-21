#### COPIED ####  VERIFIED

def find_num_activites(arr):
    # we use greedy approach. Sort based on finish times. And start selecting from beginning
    arr.sort(key=lambda x:x[1])  # Sort based on finish times

    result = []
    result.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i][0] >= result[-1][1]:  # if start of next activity is >= end of last one:
            result.append(arr[i])

    print(result)


array = [(1, 2), (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
find_num_activites(array)