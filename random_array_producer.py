import sys
import argparse
import random


def randArray(size):
  a = [random.randint(0,9999) for _ in range(size)]
  for e in a:
    e * 10000
  return a

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

array = randArray(size)
print(array)