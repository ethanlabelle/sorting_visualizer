import random

class Heap:

    def __init__(self):
        self.size = 0
        self.heap = []

    def parent(self, i):
        return int(i - 1/2)
    
    def left(self, i):
        if i == 0:
            return 1
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def heap_size(self):
        return self.size - 1

    def max_heapify(self, i):
        l = self.left(i) 
        r = self.right(i)
        if l <= self.heap_size() and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size() and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
#            print(self.heap)
            self.max_heapify(largest)
        return
    
    def heap_extract_max(self):
        if self.size < 1:
            return
        max_elm = self.heap[0]
        self.heap[0] = self.heap[self.heap_size()]
        self.size -= 1
        self.max_heapify(1)
        return max_elm

    def build_max_heap(self, array):
#        print("heap.build_max_heap(array)")
        self.size = len(array)
        self.heap = array
        for i in range(int(self.size/2), -1, -1):
            self.max_heapify(i)
        print()
#        print("MAX HEAP:") 
#        print(self.heap)
#        print()
if __name__ == "__main__":
    def heapsort(array):
        heap = Heap()
        heap.build_max_heap(array)
        for i in range(len(array) - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            heap.size -= 1
            heap.max_heapify(0)
        return array
    
    arr = [random.randint(-1000000, 1000000) for i in range(10000)]
    heapsort(arr)
    print(arr)
    pass
