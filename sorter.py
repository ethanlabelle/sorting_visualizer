from graphics import *
import random

arr_width = 1000
win = GraphWin(width=arr_width, height=arr_width)

input('''
Press Enter to Begin
''')

#print('''Choose sorting algorithm:''')
#print('''Enter:''')
#print('''\t(a) heap sort''')
#input('''\t(b) bubble sort''')
    
    # algorithm = input('''\t(quit) quit\n''')
    #if algorithm == "quit":
    #    break
    # print(algorithm)
def selection_sort(array, dim):
    for i in range(len(array)):
        min_ind = i
        for j in range(i+1, len(array)):
            if array[j][dim] < array[min_ind][dim]:
                 min_ind = j
        if min_ind != i:
            array[min_ind], array[i] = array[i], array[min_ind]
            p1 = Point(min_ind//50 * 10, min_ind%50 * 10)
            p2 = Point(min_ind//50 * 10 + 10, min_ind%50 * 10 + 10)
            rect = Rectangle(p1, p2)
            rect.setFill(color_rgb(*array[min_ind]))
            rect.setOutline(color_rgb(*array[min_ind]))
            rect.draw(win)
            
            p1 = Point(i//50 * 10, i%50 * 10)
            p2 = Point(i//50 * 10 + 10, i%50 * 10 + 10)
            rect = Rectangle(p1, p2)
            rect.setFill(color_rgb(*array[i]))
            rect.setOutline(color_rgb(*array[i]))
            rect.draw(win)
    return array

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

    def max_heapify(self, i, dim):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size() and self.heap[l][dim] > self.heap[i][dim]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size() and self.heap[r][dim] > self.heap[largest][dim]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            p1 = Point(largest//10 * 100, largest%10 * 100)
            p2 = Point(largest//10 * 100 + 100, largest%10* 100 + 100)
            rect = Rectangle(p1, p2)
            rect.setFill(color_rgb(*self.heap[largest]))
            rect.setOutline(color_rgb(*self.heap[largest]))
            rect.draw(win)
            
            p1 = Point(i//10 * 100, i%10 * 100)
            p2 = Point(i//10 * 100 + 100, i%10 * 100 + 100)
            rect = Rectangle(p1, p2)
            rect.setFill(color_rgb(*self.heap[i]))
            rect.setOutline(color_rgb(*self.heap[i]))
            rect.draw(win)
#            print(self.heap)
            self.max_heapify(largest, dim)
        return
    
    def heap_extract_max(self):
        if self.size < 1:
            return
        max_elm = self.heap[0]
        self.heap[0] = self.heap[self.heap_size()]
        self.size -= 1
        self.max_heapify(1, dim)
        return max_elm

    def build_max_heap(self, array, dim):
#        print("heap.build_max_heap(array)")
        self.size = len(array)
        self.heap = array
        for i in range(int(self.size/2), -1, -1):
            self.max_heapify(i, dim)
        print(f"MAX HEAP FINISHED dim {dim}") 
#        print(self.heap)
#        print()
def heapsort(array, dim):
    heap = Heap()
    heap.build_max_heap(array, dim)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        p1 = Point(0, 0)
        p2 = Point(100, 100)
        rect = Rectangle(p1, p2)
        rect.setFill(color_rgb(*array[0]))
        rect.setOutline(color_rgb(*array[0]))
        rect.draw(win)
            
        p1 = Point(i//10 * 100, i%10 * 100)
        p2 = Point(i//10 * 100 + 100, i%10 * 100 + 100)
        rect = Rectangle(p1, p2)
        rect.setFill(color_rgb(*array[i]))
        rect.setOutline(color_rgb(*array[i]))
        rect.draw(win)
        heap.size -= 1
        heap.max_heapify(0, dim)
    print(array)
    return array
    
array = []
for i in range(0, arr_width, 100):
    for j in range(0, arr_width, 100):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        array.append(color)        
        p1 = Point(i, j)
        p2 = Point(i+100, j+100)
        rect = Rectangle(p1, p2) 
        color = color_rgb(*color)
        print(color)
        rect.setFill(color)
        rect.setOutline(color)
        rect.draw(win)
#while True:
#    pass
# heap
print(heapsort(array, 2))
print(heapsort(array, 1))
print(heapsort(array, 0))
#print(selection_sort(array,0))
#print(selection_sort(array,2))
#print(selection_sort(array,1))

while True:
    pass
win.close()

if __name__ == "__main__":
    pass
