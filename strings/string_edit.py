### COPIED ###  VERIFIED

def remove_c_and_ab(array):
    print(array)

    k = -1  # Place to copy in the array
    i = 0
    for i in range(len(array)):
        if array[i] == 'c':  # If 'c', do nothing
            pass
        # if current is 'b' and 'a' is there in k, skip copying and remove 'a'
        elif array[i] == 'b' and k >= 0 and array[k] == 'a':
            k -= 1
        else: # anything else, copy to 'k'. Including 'a'
            k += 1
            array[k] = array[i]

    del array[k+1:]
    return array


if __name__ == '__main__':
    array = list('aaabbcacbcbcaabb')
    array = list('acbxaccbbacbycatcb')
    print(remove_c_and_ab(array))