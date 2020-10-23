from copy import deepcopy
# Python Insertion Sort Implementation

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        curr = array[i]
        while i > 0 and array[i-1]>curr:
            array[i] = array[i-1]
            i = i - 1
        array[i] = curr