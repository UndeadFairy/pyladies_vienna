"""
# store your name and age into a variable and print it in a sentense
# Save it in a script and run it from command line
name = "Elizabeth Bathory"
age = 459
print("Greetings, my noble name is", name, "and I would be", age, "years old, if I was still alive.")
"""
"""
# Calculate how long this workshop will last and store it into a new variable
# can be solved many ways, the intention was to just compute hours
# we are here using datetime.datetime and result of subtraction is datetime.timedelta
from datetime import datetime
time_now = datetime(2019, 10, 9, 16, 30)
end = datetime(2019, 10, 9, 18, 0)
left = end - time_now # datetime.timedelta
print("Still", left, "left")
"""

