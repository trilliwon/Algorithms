"""
Time Complexity
    Worst Case: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

data = [1, 2, 10, 9, 8 ,7, 4, 5, 6, 3]
selection_sort(data)
print(data)
