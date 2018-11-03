def insertion_sort(data):
    
    for i in range(1, len(data)):
        j = i
        m = data[j]
        while j > 0 and data[j-1] > m:
            data[j] = data[j-1]
            j -= 1
        data[j] = m
    return data

def bucket_sort(A):
    buckets = [[] for _ in A]
    m = max(A)

    for v in A:
        bucket_index = v * len(A) // (m+1)
        buckets[bucket_index].append(v)
    
    sorted_A = []
    for bucket in buckets:
        sorted_A.extend(insertion_sort(bucket))

    return sorted_A

data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
result = bucket_sort(data)
print(result)
