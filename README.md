# sorting-algorithms-analysis
This repository contains code to analyze the runtimes of various sorting algorithms.

https://github.com/ericdrejza/sorting-algorithms-analysis


***************** INSTRUCTIONS *****************
To run this script, first make sure you have python3 installed on your machine.
Then run in your terminal:

python3 main.py

This will produce an output in the terminal,
so if you'd like to keep a record of the output in a file,
you can redirect the output to a file by appending
"> 'file_name'" to the command above.

There are various optional arguments that I set up but the full run is the most intersting.
These helped me debug and eventually get to the full run, which provides the table of runtimes.

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Run all sorting algorithms on all array types (random,
                        half sorted, and sorted) and get their average
                        runtimes for specified array sizes
  -r, --rand, --random  Find the average runtimes for each sorting algorithm
                        on random arrays of the specified size
  -f, --full, --full-run
                        Find the average runtimes for each sorting algorithm
                        on each type of array (random, half sorted, sorted)
                        for various sizes (10, 100, 1000, 10000)
  --hs, --half-sorted   Find the average runtimes for each sorting algorithm
                        on half sorted arrays of the specified size
  -s, --sorted          Find the average runtimes for each sorting algorithm
                        on sorted arrays of the specified size
  -t, --tests           Get runtimes for each sorting algorithm on random
                        arrays of the specified size and check if the array is
                        sorted
  -n N, --num_elements N
                        Set the number of elements in the list
  --reps R              Sets the number of repitions per sort. The higher the
                        number of repitions, the closer to the true average
                        you will be


***************** CONCLUSIONS AND FINDINGS *****************
My findings are kept in records/sort_analysis.txt and contains a table similar
to the example giving in lecture slide 6c, but this is txt form (which I hope is ok).

This was a result of my own added challenge question/effort which was "how do I create a nice
looking table of my findings on my own without the use of excel?" and my implementation
is my answer to that.  This way someone wouldn't have to copy it over to excel each time
someone runs it to get the ratios of Actual/Preceding.

sorting-algorithms-analysis/records/sort_analysis.txt

***************** CITINGS AND SOURCES *****************
I used the implementation of left leaning red black trees by Peter Hillerström
and his info is listed at the top of the files within the leftrb directory.

I used our class's heapsort implementation which I think I tweaked a little bit.