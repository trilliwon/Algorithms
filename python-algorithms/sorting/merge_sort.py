
"""
p <=􏰏 q < r
"""
def merge(A, p, q, r):
    ll = q - p + 1 # left part length
    rl = r - q     # right part length

    L = [ A[p + i] for i in range(ll) ] # left
    R = [ A[q + 1 + i] for i in range(rl) ] # right

    i = j = 0
    for k in range(p, r+1):
        if i < ll and j < rl:
            if  L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        else:
            if i < ll:
                A[k] = L[i]
                i += 1
            elif j < rl:
                A[k] = R[j]
                j += 1

def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

data = [1, 2, 10, 9, 8 ,7, 4, 5, 6, 3]
merge_sort(data, 0, len(data)-1)
print(data)
