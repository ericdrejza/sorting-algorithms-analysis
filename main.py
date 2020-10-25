import sys
import argparse
from datetime import datetime
from array_producer import randArray
from bubblesort import bubblesort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from mergesort import mergesort, mergesort_insertion
from heapsort import heapsort
from bst_sort import bst_sort

#************** ARGUMENTS ******************
parser = argparse.ArgumentParser(description='Sorting Algorithms')
parser.add_argument('-a', '--all', dest='all_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('--avg', '--averages', dest='averages', action='store_const',
                    const=True, default=False)
parser.add_argument('-s', '--sorted', dest='sorted_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('-t', '--tests', dest='tests', action='store_const',
                    const=True, default=False)

args = parser.parse_args()
print(args)

if len(sys.argv) == 1:
    args.all_sorts = True

#************** FUNCTIONS ******************
def sort_and_time(array, sort_func, will_print):
    now = datetime.now()
    sort_func(array)
    elapsed = datetime.now() - now
    if will_print:
        print(str(sort_func).split()[1] + "(Runtime in Milliseconds): " + str(elapsed.microseconds/1000) + " ms")
    return elapsed

def avg_sort_and_time(sort_func, reps, num_elements, lowerBound, upperBound):
    average = datetime.min - datetime.min
    for i in range(reps):
        a = randArray(num_elements, lowerBound, upperBound)
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    # print(str(sort_func).split()[1] + "(Average): " + str(average)[2:])
    print(str(sort_func).split()[1] + "(Average Runtime in Milliseconds): " + str(average.microseconds/1000) + "ms")



#************** AVERAGES OF SORT CALLS ******************
if args.all_sorts or args.averages:
    # Find the averages of the various sorting algorithms
    print("\n".ljust(80, '-'))
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
    avg_sort_and_time(insertion_sort, REPS, NUM_ELEMENTS, LOWER_BOUND, UPPER_BOUND)

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
if args.all_sorts or args.sorted_sorts:
    print("\n".ljust(80, '-'))
    print("Runtime of Each Sorting Algorithm Using Sorted Arrays:\n")

    # Variables
    NUM_ELEMENTS_SORTED = 500
    LOWER_BOUND_SORTED = 0
    UPPER_BOUND_SORTED = NUM_ELEMENTS_SORTED * 10 - 1
    PRINT_SORTED = True

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_SORTED))
    print("Lower Bound: " + str(LOWER_BOUND_SORTED) + "; Upper Bound: " + str(UPPER_BOUND_SORTED) + "\n")

    a = list(range(0, NUM_ELEMENTS_SORTED))

    # Bubblesort
    sort_and_time(a, bubblesort, PRINT_SORTED)

    # Insertion sort
    sort_and_time(a, insertion_sort, PRINT_SORTED)

    # Selection Sort
    sort_and_time(a, selection_sort, PRINT_SORTED)

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
if args.all_sorts or args.tests:
    print("\n".ljust(80, '-'))
    print("Runtime of each sort algorithm on a random array:\n")
    
    # Variables
    NUM_ELEMENTS_TEST = 10
    LOWER_BOUND_TEST = 0
    UPPER_BOUND_TEST = NUM_ELEMENTS_TEST * 10 - 1
    PRINT_TEST = True
    
    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_TEST))
    print("Lower Bound: " + str(LOWER_BOUND_TEST) + "; Upper Bound: " + str(UPPER_BOUND_TEST) + "\n")
    

    # Bubblesort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, bubblesort, PRINT_TEST)
    print(str(a) + "\n")
    
    # Insertion sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, insertion_sort, PRINT_TEST)
    print(str(a) + "\n")

    # Selection Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, selection_sort, PRINT_TEST)
    print(str(a) + "\n")
    
    # Mergesort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, mergesort, PRINT_TEST)
    print(str(a) + "\n")
    
    # Modified Mergesort (Insertion at array size <= 8)
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, mergesort_insertion, PRINT_TEST)
    print(str(a) + "\n")
    
    # Heapsort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, heapsort, PRINT_TEST)
    print(str(a) + "\n")
    
    # BST Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, bst_sort, PRINT_TEST)
    print(str(a) + "\n")
    
    # LLRB Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    # TODO: Add LLRB sort call