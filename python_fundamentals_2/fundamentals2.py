# Remove the triple quotes to uncomment parts of code to view & run or copy parts of them to separate .py file.
"""
# Start at zero and with every iteration add 1.
# If the sum is divisible by 10 then add 15. If the sum is greater than 157, end to code.
testing_number = 0
while True:
    if testing_number % 10 == 0:
        testing_number = testing_number + 15
    if testing_number > 157:
        break
    else:
        testing_number = testing_number + 1
print(testing_number)
"""

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
"""
# Turtle create a new square using forward only twice in total.
from turtle import forward, left, Screen
def turtle_move_turn():
    forward(50)
    left(90)
for i in range(4):
    turtle_move_turn()
Screen().exitonclick()
"""
