### COPIED ###  VERIFIED

"""
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print ''.join(message)
"""


def reverse_in(l, start, end):
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1


def reverse_words(message):
    reverse_in(message, 0, len(message) - 1)

    start = 0
    end = 0

    while end < len(message):
        if message[end] == ' ':
            reverse_in(message, start, end - 1)
            start = end + 1
        elif end == len(message) - 1:  # Dont forget this condition
            reverse_in(message, start, end)
        end += 1
    print(''.join(message))


def reverse_words_without(message):
    start = 0
    l = []
    for i in range(len(message)):
        if message[i] == ' ':  # assume space wont come as the first character
            word = message[start:i]
            start = i + 1
            l.append(word)
    # Assuming ' ' wont come as last character
    word = message[start:]
    l.append(word)

    print(' '.join(l[::-1]))

if __name__ == '__main__':
    message = 'cake pound steal '
    message = ' Time is represented by Unix format '
    reverse_words(list(message))
    reverse_words_without(message)
