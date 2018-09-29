### COPIED ###  VERIFIED
"""
Given an array A, maximize value of the expression (A[s] - A[r] + A[q] - A[p])
where l, k, j and i are indexes of the input array and s > r > q > p.
We can use Dynamic Programming to solve this problem.
"""

def maximize_equation(array):
    L1 = [-float('inf')] * (len(array) + 1)
    L2 = [-float('inf')] * (len(array) + 1)
    L3 = [-float('inf')] * (len(array) + 1)
    L4 = [-float('inf')] * (len(array) + 1)

    n = len(array)

    for i in range(n-1, 2, -1):
        L1[i] = max(array[i], L1[i+1])  # Find the maximum value A[s] from backwards

    for i in range(n-2, 1, -1):
        L2[i] = max(L1[i+1] - array[i], L2[i+1])  # Find maximum A[s] - A[r]

    for i in range(n-3, 0, -1):
        L3[i] = max(L2[i+1] + array[i], L3[i+1]) # Find maximum A[s] - A[r] + A[q]

    for i in range(n-4, -1, -1):
        L4[i] = max(L3[i+1] - array[i], L4[i+1]) # Find max A[s] - A[r] + A[q] - A[p]

    return L4[0]

def maximize_equation_2(array):
    L1 = [-float('inf')] * (len(array) + 1)
    L2 = [-float('inf')] * (len(array) + 1)
    L3 = [-float('inf')] * (len(array) + 1)
    L4 = [-float('inf')] * (len(array) + 1)

    n = len(array)

    for i in range(0, n-3):
        L1[i] = max(array[i], L1[i-1])  # Find the maximum value A[s] from backwards L[i-1] = l[-1]

    for i in range(1, n-2):
        L2[i] = max(L1[i-1] - array[i], L2[i-1])  # Find maximum A[s] - A[r]

    for i in range(2, n-1):
        L3[i] = max(L2[i-1] + array[i], L3[i-1]) # Find maximum A[s] - A[r] + A[q]

    for i in range(3, n):
        L4[i] = max(L3[i-1] - array[i], L4[i-1]) # Find max A[s] - A[r] + A[q] - A[p]

    return L4[n-1]

array = [3, 9, 10, 1, 30, 40, 21]
print(maximize_equation(array))
array = [21, 40, 30, 1, 10, 9, 3]
print(maximize_equation_2(array))
