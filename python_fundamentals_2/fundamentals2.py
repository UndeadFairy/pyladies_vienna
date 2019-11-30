"""
# Write a Python program to guess a number between 1 to 9.
from random import randint
number = randint(1, 9)
repeat = True
while repeat:
    guess = input("Guess a number between 1 and 9: ")
    if int(guess) == number:
        print("Well guessed!")
        repeat = False

"""
"""
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
checked_number = 1500
while checked_number <= 2700:
    if checked_number % 35 == 0:
        print(checked_number)
        checked_number = checked_number + 35
    else:
        checked_number = checked_number + 1
"""
"""
# a function which computes area of ellipse
from math import pi

def ellipseArea(a, b):
    return pi * a * b

area1 = ellipseArea(3, 5)
print(area1)
print(ellipseArea(3.5, 4.5))


x = float(input('Insert the length of 1. axis: '))
y = float(input('Insert the length of 2. axis: '))
print(ellipseArea(x, y))
"""
