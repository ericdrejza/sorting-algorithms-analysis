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

def halfSortedArray(size, upperBound):
  a = list(range(size//2))
  b = [random.randint(size//2 + 1, upperBound) for _ in range(size//2)]
  a.extend(b)
  return a

def randHalf(a, upperBound):
  n = len(a)
  for i in range(n//2, n):
    a[i] = random.randint(n//2 + 1, upperBound)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # args = parser.parse_args()
    a = halfSortedArray(10, 100)
    print("half-sorted: " + str(a))
    a.sort()
    print("sorted: " + str(a))
    randHalf(a, 100)
    print("half-sorted: " + str(a))