'''
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print ''.join(message)
'''

def reverse_in(l, i, j):
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1


def reverse_words(message):
    reverse_in(message, 0, len(message) - 1)
    print(message)

    i = 0
    j = 0

    while j < len(message):
        if message[j] == ' ':
            reverse_in(message, i, j - 1)
            i = j + 1
        elif j == len(message) - 1:
            reverse_in(message, i, j)
        j += 1
    print(''.join(message))


if __name__ == '__main__':
    # message = 'cake pound steal'
    message = 'Time is represented by Unix format'
    reverse_words(list(message))
