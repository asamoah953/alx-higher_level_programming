#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = (number) % 10
if (number < 0):
     digit = digit
     print("Last digit of {} is {} and is ".format(number, digit), end="")
if digit > 5:
    print("greater than 5")
if(number < 6 and number !=0):
    print("less than 6 and not 0")
