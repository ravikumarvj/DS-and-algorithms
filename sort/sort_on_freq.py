#### COPIED ####
# sort based on frequency of occurence. If frequency is same, sort based on index.
def sort_on_freq(array):
    my_hash = dict()

    for index, num in enumerate(array):
        if num in my_hash:
            my_hash[num][0] += 1
        else:
            my_hash[num] = [1, index]

    my_hash = {tuple(x):y for y,x in my_hash.items()}

    result = []
    for key in sorted(my_hash.keys(), key=lambda x: (-x[0], x[1])):
        for i in range(key[0]):
            result.append(my_hash[key])

    print(result)


array = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
array = [1, 1, 2, 3, 4, 4]
sort_on_freq(array)
