#### COPIED #### VERIFIED
def print_all_rec(string, index, result):
    if index == len(string):
        print(''.join(result))

    for i in range(index, len(string)):
        result.append('{' + string[index:i+1] + '}')
        print_all_rec(string, i+1, result)
        result.pop()

    return


def print_all_substring(string):
    result = []
    print_all_rec(string, 0, result)

print_all_substring('abcd')