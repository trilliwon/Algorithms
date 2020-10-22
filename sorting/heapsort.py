


# Max heapify
class Heap(list):
    def __init__(self, a):
        list.__init__(self, a)
        self.heap_size = len(a)

    def parent(self, i):
        return i//2

    def left(self, i):
        return (i + 1) * 2 - 1

    def right(self, i):
        return (i + 1) * 2

    def max_heapify(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < self.heap_size and self[l] > self[i]:
            largest = l
        else:
            largest = i

        if r < self.heap_size and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = len(self)
        for i in range(len(self)//2, -1, -1):
            self.max_heapify(i)
    
    def heapsort(self):
        self.build_max_heap()
        for i in range(len(self)-1, 0, -1):
            self[i], self[0] = self[0], self[i] 
            self.heap_size -= 1
            self.max_heapify(0)

print('\n --- Build Max Heap ---')
data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
h = Heap(data)
h.build_max_heap()
print(h)
print('\n --- Heapsort ---')
h.heapsort()
print(h)

