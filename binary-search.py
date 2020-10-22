def binarySearch(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = [int(x) for x in input('input array ==> ').split()]
    key = int(input('input a key: '))

    index = binarySearch(arr, key)
    print("index: ", index)