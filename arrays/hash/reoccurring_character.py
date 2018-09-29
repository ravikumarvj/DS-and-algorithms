### COPIED ### VERIFIED
def delete_re_occurring(string):
    s = set()
    ret = []

    for i in string:
        if i not in s:
            s.add(i)
            ret.append(i)
    print(''.join(ret))


delete_re_occurring('aabbccacdnaaabcd')
delete_re_occurring('ravikumar')