# Python Bubblesort Implementation

# sorts the array in ascending order using the bubblesort algorithm
def bubblesort(array):
    
    # length of the array
    n = len(array)

    # flag to tell us if we have swapped this iteration
    swapped = True

    while swapped:
        # set swapped to false to start this iteration
        swapped = False
        for i in range(n - 1):
            # if the previous value is less that the next value, swap
            if array[i] > array [i + 1]:
                # swap the values at these indices
                array[i], array[i + 1] = array[i + 1], array[i]
                # set flag as swapped
                swapped = True