import sys
import argparse
from datetime import datetime
from array_producer import randArray
from bubblesort import bubblesort
from selection_sort import selection_sort

#************** ARGUMENTS ******************
parser = argparse.ArgumentParser(description='Sorting Algorithms')
parser.add_argument('-a', '--all', dest='all_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('--avg', '--averages', dest='averages', action='store_const',
                    const=True, default=False)
parser.add_argument('-s', '--sorted', dest='sorted', action='store_const',
                    const=True, default=False)
parser.add_argument('-t', '--tests', dest='tests', action='store_const',
                    const=True, default=False)

args = sys.argv
# print(args)

if len(args) == 1:
    all_sorts = True
    

#************** FUNCTIONS ******************
def sort_and_time(array, sort_func, will_print):
    now = datetime.now()
    sort_func(array)
    elapsed = datetime.now() - now
    if will_print:
        print(array)
        print(str(sort_func).split()[1] + "(Runtime in Milliseconds): " + str(elapsed.microseconds/1000) + " ms\n")
    return elapsed

def avg_sort_and_time(sort_func, reps, num_elements, lowerBound, upperBound):
    average = datetime.min - datetime.min
    for i in range(reps):
        a = randArray(num_elements, lowerBound, upperBound)
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    # print(str(sort_func).split()[1] + "(Average): " + str(average)[2:])
    print(str(sort_func).split()[1] + "(Average Runtime in Milliseconds): " + str(average.microseconds/1000) + "ms\n")



#************** AVERAGES OF SORT CALLS ******************
# Find the averages of the various sorting algorithms
print("Average Runtime of Each Sorting Algorithm:\n")

# Variables
REPS = 10
NUM_ELEMENTS = 1000
LOWER_BOUND = 0
UPPER_BOUND = NUM_ELEMENTS * 10 - 1

# Print values of the variables
print("Repitions per algorithm: " + str(REPS))
print("Number of elements in array: " + str(NUM_ELEMENTS))
print("Lower Bound: " + str(LOWER_BOUND) + "; Upper Bound: " + str(UPPER_BOUND) + "\n")

# Bubblesort
avg_sort_and_time(bubblesort, REPS, NUM_ELEMENTS, LOWER_BOUND, UPPER_BOUND)

# Insertion sort
# TODO: Add Insertion sort call

# Selection Sort
avg_sort_and_time(selection_sort, REPS, NUM_ELEMENTS, LOWER_BOUND, UPPER_BOUND)

# Mergesort
# TODO: Add Mergesort call

# Modified Mergesort (Insertion at array size <= 8)
# TODO: Add Modified Mergesort call

# Heapsort
# TODO: Add Heapsort call

# BST Sort
# TODO: Add BST sort call

# LLRB Sort
# TODO: Add LLRB sort call


#************** SORTED ARRAY SORT CALLS ******************
print("\n".ljust(80, '-'))
print("Runtime of Each Sorting Algorithm Using Sorted Arrays:\n")

# Variables
NUM_ELEMENTS_SORTED = 10
LOWER_BOUND_SORTED = 0
UPPER_BOUND_SORTED = NUM_ELEMENTS_SORTED * 10 - 1

# Print values of the variables
print("Number of elements in array: " + str(NUM_ELEMENTS_SORTED))
print("Lower Bound: " + str(LOWER_BOUND_SORTED) + "; Upper Bound: " + str(UPPER_BOUND_SORTED) + "\n")

a = randArray(NUM_ELEMENTS_SORTED, LOWER_BOUND_SORTED, UPPER_BOUND_SORTED)
selection_sort(a)

# Bubblesort
sort_and_time(a, bubblesort, True)

# Insertion sort
# TODO: Add Insertion sort call

# Selection Sort
sort_and_time(a, selection_sort, True)

# Mergesort
# TODO: Add Mergesort call

# Modified Mergesort (Insertion at array size <= 8)
# TODO: Add Modified Mergesort call

# Heapsort
# TODO: Add Heapsort call

# BST Sort
# TODO: Add BST sort call

# LLRB Sort
# TODO: Add LLRB sort call



#*********** TESTS **************
print("\n".ljust(80, '-'))
print("Runtime of Each Sorting Algorithm Using Sorted Arrays:\n")

# Variables
NUM_ELEMENTS_TEST = 10
LOWER_BOUND_TEST = 0
UPPER_BOUND_TEST = NUM_ELEMENTS_TEST * 10 - 1

# Print values of the variables
print("Number of elements in array: " + str(NUM_ELEMENTS_TEST))
print("Lower Bound: " + str(LOWER_BOUND_TEST) + "; Upper Bound: " + str(UPPER_BOUND_TEST) + "\n")

a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
# Bubblesort
sort_and_time(a, bubblesort, True)

# Insertion sort
# TODO: Add Insertion sort call

# Selection Sort
sort_and_time(a, selection_sort, True)

# Mergesort
# TODO: Add Mergesort call

# Modified Mergesort (Insertion at array size <= 8)
# TODO: Add Modified Mergesort call

# Heapsort
# TODO: Add Heapsort call

# BST Sort
# TODO: Add BST sort call

# LLRB Sort
# TODO: Add LLRB sort call