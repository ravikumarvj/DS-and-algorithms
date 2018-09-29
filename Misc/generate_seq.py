alphabets = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def generate_seq(n):
    seq = ''

    while n:
        rem = n % 26
        n //= 26
        if rem == 0: # special case
            rem = 26
            n -= 1
        seq = alphabets[rem] + seq

    return seq


print(generate_seq(25))
print(generate_seq(52))
print(generate_seq(26))
print(generate_seq(27))
print(generate_seq(103))
print(generate_seq(676))
print(generate_seq(680))
print(generate_seq(677))
print(generate_seq(750))
print(generate_seq(702))
print(generate_seq(703))
