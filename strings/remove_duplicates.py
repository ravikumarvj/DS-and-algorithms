#### COPIED #### VERIFIED
def remove_duplicates(string):
    stl = list(string)
    copy = 0
    start = 1

    while start < len(stl):
        if copy >= 0 and stl[start] == stl[copy]:
            copy -= 1
            start += 1
        else:
            copy += 1
            stl[copy] = stl[start]
            start += 1
    return ''.join(stl[:copy + 1])

def remove_one_duplicate(string):
    stl = list(string)
    copy = 0
    start = 1

    while start < len(stl):
        if stl[copy] == stl[start]:
            start += 1  # dont copy start
        else:
            copy += 1
            stl[copy] = stl[start]
            start += 1
    return ''.join(stl[:copy + 1])

if __name__ == '__main__':
    string = 'AAABBB'
    print(remove_duplicates(string))
    print(remove_one_duplicate(string))


