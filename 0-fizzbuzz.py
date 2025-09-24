#!/usr/bin/python3
""" FizzBuzz
"""

import sys


def fizzbuzz(n):
    for i in range(1, n + 1):
        # tester d'abord le cas multiple de 3 et 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        fizzbuzz(int(sys.argv[1]))
