### COPIED ###

# merge two arrays 'x' and 'y', without extra space.
# start filling with x and then y.
def merge_arrays(x, y):
    x_ptr = 0

    while x_ptr < len(x):
        if x[x_ptr] <= y[0]:
            x_ptr += 1
            continue
        x[x_ptr], y[0] = y[0], x[x_ptr]
        correct_array(y)


def correct_array(y):  # position 0 is out of order
    swap = 1
    while swap < len(y):
        if y[swap-1] <= y[swap]:
            return

        y[swap - 1], y[swap] = y[swap], y[swap - 1]
        swap += 1

ar1 = [1, 4, 7, 8, 10]
ar2 = [2, 3, 9]

merge_arrays(ar1, ar2)
print(ar1)
print(ar2)