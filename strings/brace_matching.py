### COPIED ###  VERIFIED

# Number of reverseals needed to make braces matching
# No need of stack. Just keep count of open braces.
def brace_matching(string):
    open_count = 0
    inversions = 0

    if len(string)%2:  # number of braces cannot be odd
        return float('inf')

    for brace in string:
        if brace == '{':
            open_count += 1
        else:  # close brace '}'
            if open_count == 0:
                # we cannot have a close_brace as start. So invert it.
                inversions += 1
                open_count = 1 # once reversed, it is an open brace
            else:
                open_count -= 1

    inversions += open_count//2

    return inversions


# remove unnecessary braces and return the count
def remove_unnecassary(string):
    open_count = 0
    remove_count = 0

    for brace in string:
        if brace == '{':
            open_count += 1
        else:  # Close brace '}'
            if open_count == 0:
                remove_count += 1  # remove current one
            else:
                open_count -= 1  # match and remove an open brace

    return remove_count + open_count  # open_count are currently unmatched


# remove unnecessary braces and print the balanced string
def remove_unnecassary_print(string):
    open_count = 0
    remove_count = 0
    print_list = []

    for brace in string:
        if brace == '{':
            print_list.append(brace)
            open_count += 1
        else:  # Close brace '}'
            if open_count == 0:
                remove_count += 1  # remove current one
            else:
                open_count -= 1  # match and remove an open brace
                print_list.append(brace)
                # The string so far is matched, if count == 0. Print it.
                if open_count == 0:
                    print(''.join(print_list), end='')
                    print_list = []

    print(''.join(print_list[open_count:]))


string = '}}}{'
string = '{{{{}}'
string = '}{{}}{{{'
print(brace_matching(string))
string = '{{{{}{}{{}}}'
print(remove_unnecassary(string))
remove_unnecassary_print(string)