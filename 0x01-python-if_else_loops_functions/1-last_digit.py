#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    tmp = abs(number) % 10
    lastDigit = tmp
else:
    lastDigit = number % 10


if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5", end="\n")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is zero", end="\n")
elif lastDigit < 6 and lastDigit != 0:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 and not 0", end="\n")
