import sys
import argparse

parser = argparse.ArgumentParser()
args = parser.parse_args()

if len(args) > 2:
  print("Too many arguments")
  exit

elif 