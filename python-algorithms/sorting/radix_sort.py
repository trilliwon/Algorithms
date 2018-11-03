

data = [329, 457, 657, 839, 436, 720, 355]

# O(dn)
def radix_sort(A, d):

    # counting sort to stable sort for digits
    # O(n)
    def counting_sort(A, d):
        modulus = 1
        for _ in range(d):
            modulus *= 10
        div = modulus // 10

        k = 10
        C = [ 0 for _ in range(k) ]
        B = [ 0 for _ in A ]

        assert(len(C) == k)
        assert(len(B) == len(A))

        for a in A:
            C[(a%modulus)//div] += 1 # C[i] 􏰀now contains the number of elements equal to i.

        for i in range(1, k):
            C[i] = C[i] + C[i-1] # C[i] 􏰀now contains the number of elements less than or equal to i.

        for a in A[::-1]: # iterate reversed order
            B[C[(a%modulus)//div]-1] = a
            C[(a%modulus)//div] -= 1
        
        for i in range(0, len(B)):
            A[i] = B[i]
    
    # sort A on digits
    for i in range(1, d+1):
        counting_sort(A, i)

radix_sort(data, 3)
print(data)