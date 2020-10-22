"""
Input: A sequence of n numbers <a1, a2, ... ,an>.
Output: A permutation (reordering) <a10, a20, ... , an0> i of the input sequence such that a10 􏰀a20 􏰀􏰁􏰁􏰁􏰀an0.

Insertion Sort
Time Complexity: 
    Worst Case : O(n^2) - 1+2+3+...+n-1 = n(n-1)/2
    Best Case : O(n)
Space Comlexity: O(1)
"""

def insertion_sort(data):
    
    for i in range(1, len(data)):
        j = i
        m = data[j]
        while j > 0 and data[j-1] > m:
            data[j] = data[j-1]
            j -= 1
        data[j] = m
    return data

data = [1, 2, 10, 9, 8 ,7, 4, 5, 6, 3]
insertion_sort(data)
print(data)