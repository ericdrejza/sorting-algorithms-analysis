# Python Selection Sort Implementation

def selection_sort(array):
    n = len(array)
    
    for i in range(n):
        min_val_index = i
        
        for j in range(i, n):
            if array[j] < array[min_val_index]:
                min_val_index = j
        
        if i is not min_val_index:
            array[i], array[min_val_index] = array[min_val_index], array[i]