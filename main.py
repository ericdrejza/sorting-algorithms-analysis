from datetime import datetime
from random_array_producer import randArray
from bubblesort import bubblesort

def sort_and_time(array, sort_func, print):
    now = datetime.now()
    sort_func(array)
    elapsed = datetime.now() - now
    if print:
        print(elapsed)
        print(str(sort_func).split()[1] + ": " + str(elapsed))
    return elapsed

def avg_sort_and_time(sort_func, reps, num_elements, lowerBound, upperBound):
    average = datetime.min - datetime.min
    for i in range(reps):
        a = randArray(num_elements, lowerBound, upperBound)
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    print(str(sort_func).split()[1] + "(Average): " + str(average))

# Find the averages of the various sorting algorithms
# variables for testing
REPS = 100
NUM_ELEMENTS = 1000
LOWER_BOUND = 0
UPPER_BOUND = NUM_ELEMENTS * 10 - 1

print("Repitions per algorithm: " + str(REPS))
print("Number of elements in array: " + str(NUM_ELEMENTS))
print("Lower Bound: " + str(LOWER_BOUND) + "; Upper Bound: " + str(UPPER_BOUND))

# Bubble sort
avg_sort_and_time(bubblesort, REPS, NUM_ELEMENTS, LOWER_BOUND, UPPER_BOUND)
