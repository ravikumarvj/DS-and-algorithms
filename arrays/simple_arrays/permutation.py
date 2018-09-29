### COPIED ###
"""
Given a list of array, return a list of arrays, each array is a combination of one element in each given array.
Let me give you an example to help you understand the question Suppose the input is
[[1, 2, 3], [4], [5, 6]],
the output should be
[[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].
"""

def get_permutation_recurse(array):
    if len(array) == 1:
        return [[i] for i in array[0]]

    result = []

    for i in array[0]:
        for j in get_permutation_recurse(array[1:]):
            result.append([i] + j)

    return result


def get_permutation(array):
    if len(array) == 0:
        return

    result = [[i] for i in array[0]]

    for i in array[1:]:
        temp = []  # backup array is needed because, we need to update result
                    # with each of the elements of memb, and should not put
                    # multiple members of memb together in to result
        for j in i:
            temp.extend([k + [j] for k in result])
        result = temp

    return result


if __name__ == '__main__':
    array = [[1, 2, 3], [4], [5, 6], [7, 8]]
    print(get_permutation_recurse(array))
    print(get_permutation(array))