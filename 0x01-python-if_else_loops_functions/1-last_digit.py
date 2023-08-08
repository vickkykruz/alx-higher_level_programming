#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
mul = 1
if number < 0:
    mul = -1
    num *= -1
digit = (num % 10) * mul
print("Last digit of {} is {} and ".format(number, digit), end="")
if digit > 5:
    print("is greater than 5")
elif digit == 0:
    print("is 0")
elif digit < 6:
    print("is less than 6 and not 0")
