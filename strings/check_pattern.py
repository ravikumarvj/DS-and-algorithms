def check_pattern(string, pattern):
    my_hash = {}  # Hash for character ORDER in pattern
    count = 0
    for c in pattern:
        my_hash[c] = count
        count += 1

    previous = 0  # stores the last order
    for c in string:
        if c in my_hash:  # ignore anything not in pattern
            if my_hash[c] < previous:
                print('Error')
                return
            previous = my_hash[c]  # update previous

    print('pattern is fine')
    return


check_pattern('techie deliht', 'eg')