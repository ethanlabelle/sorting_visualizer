import random
def selection_sort(array):
    for i in range(len(array)):
        min_ind = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_ind]:
                min_ind = j
        if min_ind != i:
            array[min_ind], array[i] = array[i], array[min_ind]
    
    return array

array = [random.randint(-1000000, 1000000) for i in range(10000)]

selection_sort(array)
