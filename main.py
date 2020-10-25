import sys
import argparse
from math import log10
from datetime import datetime
from array_producer import randArray, halfSortedArray, randHalf
from bubblesort import bubblesort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from mergesort import mergesort, mergesort_insertion
from heapsort import heapsort
from bst_sort import bst_sort
from leftrb.llrb import leftrb_sort

#************** ARGUMENTS ******************
parser = argparse.ArgumentParser(description='Sorting Algorithms')
parser.add_argument('-a', '--all', dest='all_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('--avg', '--averages', dest='averages', action='store_const',
                    const=True, default=False)
parser.add_argument('--half-sorted', dest='half_sorted_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('-s', '--sorted', dest='sorted_sorts', action='store_const',
                    const=True, default=False)
parser.add_argument('-t', '--tests', dest='tests', action='store_const',
                    const=True, default=False)

args = parser.parse_args()

if len(sys.argv) == 1:
    args.all_sorts = True

LJUST_SPACING = 64

#************** FUNCTIONS ******************
def sort_and_time(array, sort_func, will_print):
    now = datetime.now()
    sort_func(array)
    elapsed = datetime.now() - now
    if will_print:
        print(str(sort_func).split()[1] + "(Runtime in Milliseconds): " + str(elapsed.microseconds/1000) + " ms")
    return elapsed

def avg_rand_array_sort_and_time(sort_func, num_elements, reps, lowerBound, upperBound):
    average = datetime.min - datetime.min
    for i in range(reps):
        a = randArray(num_elements, lowerBound, upperBound)
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    average_milliseconds = average.microseconds/1000
    print((str(sort_func).split()[1] + "(Average Runtime in Milliseconds): ").ljust(LJUST_SPACING - len(str(average.microseconds).split('.')[0]), ' ') + \
        runtime_string(average_milliseconds) + "ms")
    return average

def avg_sorted_array_sort_and_time(sort_func, num_elements, reps):
    average = datetime.min - datetime.min
    a = list(range(num_elements))
    for i in range(reps):
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    average_milliseconds = average.microseconds/1000
    print((str(sort_func).split()[1] + "(Average Runtime in Milliseconds): ").ljust(LJUST_SPACING - len(str(average.microseconds).split('.')[0]), ' ') + \
        runtime_string(average_milliseconds) + "ms")
    return average

def avg_half_sorted_array_sort_and_time(sort_func, num_elements, reps, upperBound):
    average = datetime.min - datetime.min
    a = halfSortedArray(num_elements, upperBound)
    for i in range(reps):
        average += sort_and_time(a, sort_func, False)
        randHalf(a, upperBound)
    average = average / reps
    average_milliseconds = average.microseconds/1000
    print((str(sort_func).split()[1] + "(Average Runtime in Milliseconds): ").ljust(LJUST_SPACING - len(str(average.microseconds).split('.')[0]), ' ') + \
        runtime_string(average_milliseconds) + "ms")
    return average

def runtime_string(milliseconds):
    return str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0')


#************** RANDOM ARRAY SORT CALLS ******************
if args.all_sorts or args.averages:
    # Find the averages of the various sorting algorithms
    print("\n".ljust(80, '-'))
    print("Average Runtime of Each Sorting Algorithm:\n")

    # Variables
    NUM_ELEMENTS = 1000
    REPS = 10
    LOWER_BOUND = 0
    UPPER_BOUND = NUM_ELEMENTS * 10 - 1

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS))
    print("Repitions per algorithm: " + str(REPS))
    print("Lower Bound: " + str(LOWER_BOUND) + "; Upper Bound: " + str(UPPER_BOUND) + "\n")

    # Bubblesort
    avg_rand_array_sort_and_time(bubblesort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # Insertion sort
    avg_rand_array_sort_and_time(insertion_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # Selection Sort
    avg_rand_array_sort_and_time(selection_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # Mergesort
    avg_rand_array_sort_and_time(mergesort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # Modified Mergesort (Insertion at array size <= 8)
    avg_rand_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # Heapsort
    avg_rand_array_sort_and_time(heapsort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # BST Sort
    avg_rand_array_sort_and_time(bst_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)

    # LLRB Sort
    avg_rand_array_sort_and_time(leftrb_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)


#************** SORTED ARRAY SORT CALLS ******************
if args.all_sorts or args.sorted_sorts:
    print("\n".ljust(80, '-'))
    print("Runtime of Each Sorting Algorithm Using Sorted Arrays:\n")

    # Variables
    NUM_ELEMENTS_SORTED = 100
    REPS_SORTED = 10
    PRINT_SORTED = True

    sys.setrecursionlimit(10**6)

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_SORTED))
    print("Repitions per algorithm: " + str(REPS_SORTED) + "\n")

    a = list(range(0, NUM_ELEMENTS_SORTED))

    # Bubblesort
    avg_sorted_array_sort_and_time(bubblesort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # Insertion sort
    avg_sorted_array_sort_and_time(insertion_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # Selection Sort
    avg_sorted_array_sort_and_time(selection_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # Mergesort
    avg_sorted_array_sort_and_time(mergesort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # Modified Mergesort (Insertion at array size <= 8)
    avg_sorted_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # Heapsort
    avg_sorted_array_sort_and_time(heapsort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # BST Sort
    avg_sorted_array_sort_and_time(bst_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)

    # LLRB Sort
    avg_sorted_array_sort_and_time(leftrb_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)


#************** HALF SORTED ARRAY SORT CALLS ******************
if args.all_sorts or args.half_sorted_sorts:
    # Find the averages of the various sorting algorithms
    print("\n".ljust(80, '-'))
    print("Average Runtime of Each Sorting Algorithm Using Half Sorted Arrays:\n")

    # Variables
    NUM_ELEMENTS_HALF_SORTED = 1000
    REPS_HALF_SORTED = 10
    UPPER_BOUND_HALF_SORTED = NUM_ELEMENTS_HALF_SORTED * 10 - 1

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_HALF_SORTED))
    print("Repitions per algorithm: " + str(REPS_HALF_SORTED))
    print("Upper Bound: " + str(UPPER_BOUND_HALF_SORTED) + "\n")

    # Bubblesort
    avg_half_sorted_array_sort_and_time(bubblesort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # Insertion sort
    avg_half_sorted_array_sort_and_time(insertion_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # Selection Sort
    avg_half_sorted_array_sort_and_time(selection_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # Mergesort
    avg_half_sorted_array_sort_and_time(mergesort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # Modified Mergesort (Insertion at array size <= 8)
    avg_half_sorted_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # Heapsort
    avg_half_sorted_array_sort_and_time(heapsort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # BST Sort
    avg_half_sorted_array_sort_and_time(bst_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)

    # LLRB Sort
    avg_half_sorted_array_sort_and_time(leftrb_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)


#*********** TESTS **************
if args.tests:
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
    sort_and_time(a, leftrb_sort, PRINT_TEST)
    print(str(a) + "\n")