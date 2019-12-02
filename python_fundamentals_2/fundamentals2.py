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
"""
# 2. Using functions penup and pendown you can say turtle to stop and continue drawing. Draw a dashed line.
from turtle import forward, left, Screen, penup, pendown
for i in range(30):
    pendown()
    forward(10)
    left(12)
    penup()
    forward(10)
    
Screen().exitonclick()
"""
"""
# 3. Draw 3 squares, each turned by 20°
from turtle import forward, left, Screen
def draw_house(length_of_side):
    for j in range(4):
        forward(length_of_side)
        left(90)
for i in range(3):
    draw_house(150)
    left(20)
Screen().exitonclick()
"""
"""
# 4. Draw a rainbow
from turtle import width, pencolor, left, forward, Screen
colors = ['red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'purple']
left(90)
width(30)
for color in colors:
    pencolor(color)
    forward(50)
    left(-180 / len(colors) - 3)
Screen().exitonclick()
"""
"""
# 1. Write a program to get the smallest number from a list.
test_list = [25, 13.34, -43, 105]
# sort() method modifies the list "in place"
test_list.sort()
smallest = test_list[0]
print(smallest, test_list)
"""
"""
# 2. Write a program to sum all the items in a list.
test_list = [25, 13.34, -43, 105]
summed = sum(test_list)
print(summed)
"""
"""
# 3. Write a function to print a list after removing the 0th, 4th and 5th elements.
def remove_ugly_elements(list_to_modify):
    del list_to_modify[5]
    del list_to_modify[4]
    del list_to_modify[0]
    print(list_to_modify)
remove_ugly_elements([12, 13, 14, 15, 16, 17, 18, 19, 20])
"""
"""
# 4. Write a program to shuffle and print 1st element of new list
from random import shuffle
test_list = [12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(test_list)
print(test_list[1])
"""