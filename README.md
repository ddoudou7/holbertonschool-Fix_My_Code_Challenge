# Fix My Code Challenge

This repository contains my solutions for the **Fix my code** project at Holberton School.

## Task 0: FizzBuzz (Python)

- **Bug**: 15 was printing Fizz instead of FizzBuzz.
- **Cause**: the condition `i % 3 == 0` was checked before `i % 3 == 0 and i % 5 == 0`, so the common case was never reached.
- **Fix**: check multiples of both 3 and 5 first, then 3, then 5.
- **Expected result**:
```bash
./0-fizzbuzz.py 20
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
```

## Environment
- Ubuntu 20.04 LTS  
- Python 3.8.5  

## Usage
```bash
chmod +x 0-fizzbuzz.py
./0-fizzbuzz.py <number>
```

Example:
```bash
./0-fizzbuzz.py 50
```

## Author
Project completed as part of the **Holberton School** curriculum.
