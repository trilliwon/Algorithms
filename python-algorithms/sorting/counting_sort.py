


def counting_sort(A, k):
    C = [ 0 for _ in range(k+1) ]
    B = [ 0 for _ in A ]

    assert(len(C) == k+1)
    assert(len(B) == len(A))

    for j in A:
        C[j] += 1 # C[i] 􏰀now contains the number of elements equal to i.

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1] # C[i ]􏰀now contains the number of elements less than or equal to i.

    for a in A[::-1]: # iterate reversed order
        B[C[a]-1] = a
        C[a] = C[a] - 1

    return B

data = [2, 5, 3, 0, 2, 3, 0, 3]
result = counting_sort(data, 5)
print(result)