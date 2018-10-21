#### COPIED ####  VERIFIED
def find_max(string, k, index):
    max_so_far = int(''.join(string))
    find_max.count += 1

    if k == 0:
        return max_so_far

    for i in range(index, len(string)):
        for j in range(i + 1, len(string)):
            if string[i] < string[j]:
                string[i], string[j] = string[j], string[i]
                ret = find_max(string, k-1, i+1)
                max_so_far = max(max_so_far, ret, int(''.join(string)))
                string[i], string[j] = string[j], string[i]

    return max_so_far


def find_max_k_swap(string, k):
    string_list = list(string)
    find_max.count = 0
    ret = find_max(string_list, k, 0)
    print(find_max.count)
    return ret

print(find_max_k_swap('12345678912345678910', 3))
