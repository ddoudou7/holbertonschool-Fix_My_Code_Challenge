#!/usr/bin/python3
"""
FizzBuzz: print numbers from 1 to n separated by a single space.
- Multiples of 3     -> "Fizz"
- Multiples of 5     -> "Buzz"
- Multiples of 3 & 5 -> "FizzBuzz"
"""

import sys


def fizzbuzz(n: int) -> None:
    if n < 1:
        return
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    print(" ".join(out))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid number")
        sys.exit(1)
    fizzbuzz(number)
