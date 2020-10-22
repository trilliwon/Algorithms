





def maximum(data, low, high):
    if high==low:
        return data[low]
    mid = int((low+high)//2)
    left = maximum(data, low, mid)
    right = maximum(data, mid+1, high)
    print(left, right)
    return max(left, right)

data = [2, 10, 3, 4, 6, 7, 8, 9, 0, 1]

result = maximum(data, 0, len(data)-1)

print(data)
print('max: ' + str(result))
