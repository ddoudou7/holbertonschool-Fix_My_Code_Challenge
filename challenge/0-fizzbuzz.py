#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)

    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    print(" ".join(result))
