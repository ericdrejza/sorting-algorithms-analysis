import sys
import argparse
import random

# Returns an array of random integer elements between the range of 0 and 9999
# Size of the array is determined by the size arument
def randArray(size, lowerBound, upperBound):
  a = [random.randint(lowerBound, upperBound) for _ in range(size)]
  for e in a:
    e * 10000
  return a

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # args = parser.parse_args()
    args = sys.argv
    print(args)
    print(len(args))

    if len(args) > 2:
      print("Too many arguments")
      exit
    elif len(args) == 1:
      size = int(input("How many elements? "))
    else:
      size = int(args[1])

    array = randArray(size, 0, 100)
    print(array)