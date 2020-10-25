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
                    const=True, default=False,
                    help='Run all sorting algorithms on all array types (random, half sorted, and sorted) and get their average runtimes for specified array sizes')
parser.add_argument('-r', '--rand', '--random', dest='random', action='store_const',
                    const=True, default=False,
                    help='Find the average runtimes for each sorting algorithm on random arrays of the specified size')
parser.add_argument('-f', '--full', '--full-run', dest='full_run', action='store_const',
                    const=True, default=False,
                    help='Find the average runtimes for each sorting algorithm on each type of array (random, half sorted, sorted) for various sizes (10, 100, 1000, 10000)')
parser.add_argument('--hs', '--half-sorted', dest='half_sorted_sorts', action='store_const',
                    const=True, default=False,
                    help='Find the average runtimes for each sorting algorithm on half sorted arrays of the specified size')
parser.add_argument('-s', '--sorted', dest='sorted_sorts', action='store_const',
                    const=True, default=False,
                    help='Find the average runtimes for each sorting algorithm on sorted arrays of the specified size')
parser.add_argument('-t', '--tests', dest='tests', action='store_const',
                    const=True, default=False,
                    help='Get runtimes for each sorting algorithm on random arrays of the specified size and see the sorted array')

parser.add_argument('-n', '--num_elements', metavar='N', dest='num_elements', type=int,
                    help='Set the number of elements in the list')
parser.add_argument('--reps', metavar='R', dest='num_reps', type=int,
                    help='Sets the number of repitions per sort.  The higher the number of repitions, the closer to the true average you will be')

args = parser.parse_args()

if len(sys.argv) == 1:
    args.full_run = True

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
    run_string = runtime_string(average_milliseconds, sort_func)
    return (average_milliseconds, run_string)

def avg_sorted_array_sort_and_time(sort_func, num_elements, reps):
    average = datetime.min - datetime.min
    a = list(range(num_elements))
    for i in range(reps):
        average += sort_and_time(a, sort_func, False)
    average = average / reps
    average_milliseconds = average.microseconds/1000
    run_string = runtime_string(average_milliseconds, sort_func)
    return (average_milliseconds, run_string)

def avg_half_sorted_array_sort_and_time(sort_func, num_elements, reps, upperBound):
    average = datetime.min - datetime.min
    a = halfSortedArray(num_elements, upperBound)
    for i in range(reps):
        average += sort_and_time(a, sort_func, False)
        randHalf(a, upperBound)
    average = average / reps
    average_milliseconds = average.microseconds/1000
    run_string = runtime_string(average_milliseconds, sort_func)
    return (average_milliseconds, run_string)

def runtime_string(milliseconds , sort_func):
    return (str(sort_func).split()[1] + ' ' + "(Average Runtime in Milliseconds): ").ljust(LJUST_SPACING - len(str(milliseconds).split('.')[0]), ' ') + \
        str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0') + "ms"

def isSorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

#************** RANDOM ARRAY SORT CALLS ******************
if args.all_sorts or args.random:
    # Find the averages of the various sorting algorithms
    print("\n".ljust(80, '-'))
    print("Average Runtime of Each Sorting Algorithm Using Random Arrays:\n")

    # Variables
    if args.num_elements == None:
        NUM_ELEMENTS = 1000
    else:
        NUM_ELEMENTS = args.num_elements
        
    if args.num_reps == None:
        REPS = 10
    else:
        REPS = args.num_reps
    LOWER_BOUND = 0
    UPPER_BOUND = NUM_ELEMENTS * 10 - 1

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS))
    print("Repitions per algorithm: " + str(REPS))
    print("Lower Bound: " + str(LOWER_BOUND) + "; Upper Bound: " + str(UPPER_BOUND) + "\n")

    # Bubblesort
    print(avg_rand_array_sort_and_time(bubblesort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # Insertion sort
    print(avg_rand_array_sort_and_time(insertion_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # Selection Sort
    print(avg_rand_array_sort_and_time(selection_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # Mergesort
    print(avg_rand_array_sort_and_time(mergesort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # Modified Mergesort (Insertion at array size <= 8)
    print(avg_rand_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # Heapsort
    print(avg_rand_array_sort_and_time(heapsort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # BST Sort
    print(avg_rand_array_sort_and_time(bst_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])

    # LLRB Sort
    print(avg_rand_array_sort_and_time(leftrb_sort, NUM_ELEMENTS, REPS, LOWER_BOUND, UPPER_BOUND)[1])


#************** HALF SORTED ARRAY SORT CALLS ******************
if args.all_sorts or args.half_sorted_sorts:
    # Find the averages of the various sorting algorithms
    print("\n".ljust(80, '-'))
    print("Average Runtime of Each Sorting Algorithm Using Half Sorted Arrays:\n")

    # Variables
    if args.num_elements == None:
        NUM_ELEMENTS_HALF_SORTED = 1000
    else:
        NUM_ELEMENTS_HALF_SORTED = args.num_elements

    if args.num_reps == None:
        REPS_HALF_SORTED = 10
    else:
        REPS_HALF_SORTED = args.num_reps

    UPPER_BOUND_HALF_SORTED = NUM_ELEMENTS_HALF_SORTED * 10 - 1

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_HALF_SORTED))
    print("Repitions per algorithm: " + str(REPS_HALF_SORTED))
    print("Upper Bound: " + str(UPPER_BOUND_HALF_SORTED) + "\n")

    # Bubblesort
    print(avg_half_sorted_array_sort_and_time(bubblesort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # Insertion sort
    print(avg_half_sorted_array_sort_and_time(insertion_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # Selection Sort
    print(avg_half_sorted_array_sort_and_time(selection_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # Mergesort
    print(avg_half_sorted_array_sort_and_time(mergesort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # Modified Mergesort (Insertion at array size <= 8)
    print(avg_half_sorted_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # Heapsort
    print(avg_half_sorted_array_sort_and_time(heapsort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # BST Sort
    print(avg_half_sorted_array_sort_and_time(bst_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])

    # LLRB Sort
    print(avg_half_sorted_array_sort_and_time(leftrb_sort, NUM_ELEMENTS_HALF_SORTED, REPS_HALF_SORTED, UPPER_BOUND_HALF_SORTED)[1])


#************** SORTED ARRAY SORT CALLS ******************
if args.all_sorts or args.sorted_sorts:
    print("\n".ljust(80, '-'))
    print("Runtime of Each Sorting Algorithm Using Sorted Arrays:\n")

    # Variables
    if args.num_elements == None:
        NUM_ELEMENTS_SORTED = 1000
    else:
        NUM_ELEMENTS_SORTED = args.num_elements

    if args.num_reps == None:
        REPS_SORTED = 10
    else:
        REPS_SORTED = args.num_reps
    PRINT_SORTED = True

    sys.setrecursionlimit(10**6)

    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_SORTED))
    print("Repitions per algorithm: " + str(REPS_SORTED) + "\n")

    a = list(range(0, NUM_ELEMENTS_SORTED))

    # Bubblesort
    print(avg_sorted_array_sort_and_time(bubblesort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # Insertion sort
    print(avg_sorted_array_sort_and_time(insertion_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # Selection Sort
    print(avg_sorted_array_sort_and_time(selection_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # Mergesort
    print(avg_sorted_array_sort_and_time(mergesort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # Modified Mergesort (Insertion at array size <= 8)
    print(avg_sorted_array_sort_and_time(mergesort_insertion, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # Heapsort
    print(avg_sorted_array_sort_and_time(heapsort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # BST Sort
    print(avg_sorted_array_sort_and_time(bst_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])

    # LLRB Sort
    print(avg_sorted_array_sort_and_time(leftrb_sort, NUM_ELEMENTS_SORTED, REPS_SORTED)[1])


#*********** TESTS **************
if args.tests:
    print("\n".ljust(80, '-'))
    print("Runtime of each sort algorithm on a random array:\n")
    
    # Variables
    NUM_ELEMENTS_TEST = 10000
    LOWER_BOUND_TEST = 0
    UPPER_BOUND_TEST = NUM_ELEMENTS_TEST * 10 - 1
    PRINT_TEST = True
    
    # Print values of the variables
    print("Number of elements in array: " + str(NUM_ELEMENTS_TEST))
    print("Lower Bound: " + str(LOWER_BOUND_TEST) + "; Upper Bound: " + str(UPPER_BOUND_TEST) + "\n")
    

    # Bubblesort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, bubblesort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # Insertion sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, insertion_sort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))

    # Selection Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, selection_sort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # Mergesort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, mergesort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # Modified Mergesort (Insertion at array size <= 8)
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, mergesort_insertion, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # Heapsort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, heapsort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # BST Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, bst_sort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))
    
    # LLRB Sort
    a = randArray(NUM_ELEMENTS_TEST, LOWER_BOUND_TEST, UPPER_BOUND_TEST)
    sort_and_time(a, leftrb_sort, PRINT_TEST)
    print("Is sorted: " + str(isSorted(a)))\
    
if args.full_run:

    # Variables
    if args.num_reps == None:
        REPS_FULL = 10
    else:
        REPS_FULL = args.num_reps
    LOWER_BOUND_FULL = 0

    print("Repitions per sort: " + str(REPS_FULL) + '\n')
    
    sys.setrecursionlimit(10**6)

    sorts = (bubblesort, insertion_sort, selection_sort, mergesort, mergesort_insertion, heapsort, bst_sort, leftrb_sort)
    sizes = (10, 100, 1000, 10000)
    array_types = (avg_rand_array_sort_and_time, avg_sorted_array_sort_and_time, avg_half_sorted_array_sort_and_time)

    # (str(sort_func).split()[1] + ' ' + "(Average Runtime in Milliseconds): ").ljust(LJUST_SPACING - len(str(milliseconds).split('.')[0]), ' ') + \
    #     str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0') + "ms"

    SIZE_LJUST = len("SIZE") + 10
    RAND_ARRAY_LJUST = len("RANDOM (ms)") + 5
    HALF_SORTED_ARRAY_LJUST = len("HALF SORTED (ms)")+ 5
    SORTED_ARRAY_LJUST = len("FULL SORTED (ms)") + 5
    RATIO_LJUST = len("ACTUAL/PRECEDING") + 15

    for sort in sorts:
        print(str(sort).split()[1] + ":\n" + \
            "SIZE".ljust(SIZE_LJUST) + "RANDOM (ms)".ljust(RAND_ARRAY_LJUST) + "ACTUAL/PRECEDING".ljust(RATIO_LJUST) +\
                "HALF SORTED (ms)".ljust(HALF_SORTED_ARRAY_LJUST) + "ACTUAL/PRECEDING".ljust(RATIO_LJUST) + \
                    "FULL SORTED (ms)".ljust(SORTED_ARRAY_LJUST) + "ACTUAL/PRECEDING")

        PRECEDING = [0, 0, 0]

        for size in sizes:
            UPPER_BOUND_FULL = size * 10 -1

            string = (str(size) + ": ").ljust(SIZE_LJUST)

            # RANDOM ARRAY
            milliseconds = avg_rand_array_sort_and_time(sort, size, REPS_FULL, LOWER_BOUND_FULL, UPPER_BOUND_FULL)[0]
            # print(milliseconds)
            string = string + (str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0')).ljust(RAND_ARRAY_LJUST)
            
            # RANDOM ARRAY: ACTUAL / PRECEDING
            if (PRECEDING[0] != 0):
                ratio = round(milliseconds / PRECEDING[0], 1)
            else:
                ratio = "---"
            PRECEDING[0] = milliseconds
            string = string + str(ratio).ljust(RATIO_LJUST)


            # HALF SORTED
            milliseconds  = avg_half_sorted_array_sort_and_time(sort, size, REPS_FULL, UPPER_BOUND_FULL)[0]
            # print(milliseconds)
            string = string + (str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0') + ' ').ljust(HALF_SORTED_ARRAY_LJUST)
            
            # HALF SORTED ARRAY: ACTUAL / PRECEDING 
            if (PRECEDING[1] != 0):
                ratio = round(milliseconds / PRECEDING[1], 1)
            else:
                ratio = "---"
            PRECEDING[1] = milliseconds
            string = string + str(ratio).ljust(RATIO_LJUST)


            # SORTED
            milliseconds = avg_sorted_array_sort_and_time(sort, size, REPS_FULL)[0]
            # print(milliseconds)
            string = string + (str(milliseconds).split('.')[0] + '.' + str(milliseconds).split('.')[1].ljust(3, '0')).ljust(SORTED_ARRAY_LJUST)

            # SORTED ARRAY: ACTUAL / PRECEDING 
            if (PRECEDING[2] != 0):
                ratio = round(milliseconds / PRECEDING[2], 1)
            else:
                ratio = "---"
            PRECEDING[2] = milliseconds
            string = string + str(ratio)

            print(string)
        
        print()
            