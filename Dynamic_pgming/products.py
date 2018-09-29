#### COPIED ####  VERIFIED
def product_except_index(array):
    if len(array) <= 1:
        return array

    before = [array[i] for i in range(len(array))]
    after = [array[i] for i in range(len(array))]

    product = [0 for i in range(len(array))]

    for i in range(1, len(array)):
        before[i] = before[i-1] * array[i]
    for i in range(len(array) - 2, -1, -1):
        after[i] = after[i+1] * array[i]

    product[0] = after[1]
    for i in range(1, len(array) - 1):
        product[i] = before[i-1] * after[i+1]
    product[-1] = before[-2]

    return product

def product_except_index_save_space(array):
    if len(array) <= 1:
        return array

    after = [0] * len(array)

    product = 1
    for i in range(len(array) - 1, -1, -1):
        product *= array[i]
        after[i] = product

    product = 1
    for i in range(0, len(array)-1):
        after[i] = after[i+1] * product
        product *= array[i]
    after[-1] = product

    return after


if __name__ == '__main__':
    array=[2, 4, 5, 10, 5, 2]
    print(product_except_index(array))
    print(product_except_index_save_space(array))