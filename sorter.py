from graphics import *
import random
import cProfile
import math

window_width = 500
n = 100
row_size = int(math.sqrt(n))
assert row_size * row_size == n
win = GraphWin(width=window_width, height=window_width)
array = []
board = []
square_width = int(window_width/row_size)

algo = None
while not algo:
    algo = input('''Choose a sort
    a) Heapsort
    b) Mergesort
    c) Selection Sort
    ''')


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
            board[largest].setFill(color_rgb(*self.heap[largest]))
            board[largest].setOutline(color_rgb(*self.heap[largest]))
            board[i].setFill(color_rgb(*self.heap[i]))
            board[i].setOutline(color_rgb(*self.heap[i]))
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
        self.size = len(array)
        self.heap = array
        for i in range(int(self.size/2), -1, -1):
            self.max_heapify(i, dim)
        print(f"MAX HEAP FINISHED dim {dim}") 

def heapsort(array, dim):
    heap = Heap()
    heap.build_max_heap(array, dim)
    for i in range(len(array) - 1, 0, -1):
        # remove max element
        array[0], array[i] = array[i], array[0]
        heap.size -= 1
        # update tiles
        board[0].setFill(color_rgb(*array[0]))
        board[0].setOutline(color_rgb(*array[0]))
        board[i].setFill(color_rgb(*array[i]))
        board[i].setOutline(color_rgb(*array[i]))
        # update heap
        heap.max_heapify(0, dim)
    print(array)
    return array
 
def mergesort(array, dim, start, stop):
    if len(array[start:stop]) <= 1:
        return
    else:
        split = int((start + stop)/2)
        mergesort(array, dim, start, split)
        mergesort(array, dim, split, stop)
        i = start
        j = split
        merged = []
        while i < split or j < stop:
            if i < split and j < stop:
                if array[i][dim] < array[j][dim]:
                    merged.append(array[i])
                    i += 1
                else:
                    merged.append(array[j])
                    j += 1
            elif i < split:
                merged += array[i:split]
                break
            elif j < stop:
                merged += array[j:stop]
                break
        for k in range(len(merged)):
            array[start + k] = merged[k]
            color = color_rgb(*array[start + k])
            board[start + k].setFill(color)
            board[start + k].setOutline(color)
        return

def selection(array, dim):
    for i in range(len(array)):
        min_ind = i 
        for j in range(i, len(array)):
            if array[j][dim] < array[min_ind][dim]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]
        board[i].setFill(color_rgb(*array[i]))
        board[i].setOutline(color_rgb(*array[i]))
        board[min_ind].setFill(color_rgb(*array[min_ind]))
        board[min_ind].setOutline(color_rgb(*array[min_ind]))



for i in range(0, row_size*square_width, square_width):
    for j in range(0, row_size*square_width, square_width):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        array.append(color)        
        p1 = Point(i, j)
        p2 = Point(i+square_width, j+square_width)
        rect = Rectangle(p1, p2) 
        color = color_rgb(*color)
        print(color)
        rect.setFill(color)
        rect.setOutline(color)
        rect.draw(win)
        board.append(rect)

# heap
if algo == 'a':
    heapsort(array, 0)
elif algo == 'b':
    mergesort(array, 1, 0, n)
elif algo == 'c':
    selection(array, 0)
else:
    print("try again")

#cProfile.run('heapsort(array, 2)') 

input("press enter to close")
win.close()
