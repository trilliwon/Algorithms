"""
Worst Case: O(N^2)
Average Case: O(NLogN)
"""
import random

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def partition(A, p, r):
    pivot = A[r]

    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)    

data = [1, 2, 10, 9, 8 ,7, 4, 5, 6, 3]
quick_sort(data, 0, len(data)-1)
print("Quicksort")
print(data)

randomized_quicksort(data, 0, len(data)-1)
print("\nRandomized Quicksort")
print(data)