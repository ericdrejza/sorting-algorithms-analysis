# Python Mergesort Implementation - Structure from Lecture Slides 5b

from insertion_sort import insertion_sort

def mergesort(array):
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]

        # mergesort on both halves
        mergesort(left)
        mergesort(right)

        # merge
        merge(array, left, right)


def mergesort_insertion(array):
    n = len(array)
    if n > 8:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]

        # mergesort on both halves
        mergesort(left)
        mergesort(right)

        # merge
        merge(array, left, right)
    else:
        insertionSort(array)


def merge(array, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1

