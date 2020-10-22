"""
Time Complexity
"""

def bubble_sort(data):
	for i in range(len(data)):
        # swapped = False, if False return
		for j in range(len(data)-i-1):
			if data[j] > data[j+1]:
                # swapped = True
				data[j], data[j+1] = data[j+1], data[j]
	return data

data = [1, 2, 10, 9, 8 ,7, 4, 5, 6, 3]
bubble_sort(data)
print(data)