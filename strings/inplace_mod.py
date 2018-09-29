def in_place_mod(string):  # delete string[i] is O(N) operation
    i = 0
    while i < len(string):
        if string[i] == 'c':
            del string[i]
            if i-1 >= 0 and string[i-1] == 'a':
                i -= 1
        elif i+1 < len(string) and string[i] == 'a' and string[i+1] == 'b':
            del string[i + 1]  # First delete string i+1
            del string[i]

            if i-1 >= 0 and string[i-1] == 'a':
                i -= 1
        else:
            i += 1
    return string


def in_place_mod_eff(string):
    i = 0
    k = 0
    while i < len(string):
        if k > 0 and string[k - 1] == 'a' and string[i] == 'b':
            k -= 1
            i += 1
        elif string[i] == 'c':
            i += 1
        else:
            string[k] = string[i]
            i += 1
            k += 1
    del string[k:]
    return string


if __name__ == '__main__':
    s = 'acbxaccbbacbycatcb'

    string = list(s)
    print(''.join(in_place_mod(string)))
    string = list(s)
    print(''.join(in_place_mod_eff(string)))