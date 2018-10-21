#### COPIED ####   VERIFIED

alpha = list('abcdefghijklmnopqrstuvwxyz')

def convert_to_string(num):
    if num <= 0:
        return
    string = []

    while num:
        rem = num % 26
        # treat remainder zero as special case.
        if rem == 0:
            rem = 26
            num -= 1

        string.append(alpha[rem - 1]) # -1 needed, because alpha starts at 0
        num //= 26

    print(''.join(string[::-1]))


if __name__ == '__main__':
    convert_to_string(962)
    convert_to_string(549)
    convert_to_string(572)
    convert_to_string(485)
    convert_to_string(704)


"""
585 &#8211; VM<br />
873 &#8211; AGO<br />
269 &#8211; JI<br />
849 &#8211; AFQ<br />
288 &#8211; KB<br />
962 &#8211; AJZ<br />
549 &#8211; UC<br />
572 &#8211; UZ<br />
485 &#8211; RQ<br />
704 &#8211; AAB<br />
"""