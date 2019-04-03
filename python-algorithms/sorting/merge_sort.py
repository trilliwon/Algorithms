
"""
p <=􏰏 q < r
"""
def merge(A, low, mid, high):
    H = [x for x in A]
    left = low
    right = mid + 1
    s = low
    while left <= mid and right <= high:
        if H[left] <= H[right]:
            A[s] = H[left]
            left += 1
        else:
            A[s] = H[right]
            right += 1
        
        s += 1
        remaining = (mid - left) + 1

        for i in range(remaining):
            A[s + i] = H[left + i]

def merge_sort(A, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid + 1, high)
        merge(A, low, mid, high)

data = [1, 2, 0, 0, -1, -20, 10, 9, 8 ,7, 7, 4, 5, 6, 3]
merge_sort(data, 0, len(data)-1)
print(data)
