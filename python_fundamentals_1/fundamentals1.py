import operator

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

for i in range(5):
    print('Row %s' % i)

# Operator thing
print('Take 2 numbers and do basic math operation (operator package!).')
number_one = int(input('Give me first number: (e. g.: 846486465)'))
number_two = int(input('Give me second number: (e. g.: 846486465)'))
input_op = input('Give me what to do with them: (+, -, /, *)')


ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
for k, in ops.keys():
    if input_op == k:
        print(ops[k](number_one, number_two))


# Min, Max
print("Take 5 numbers and return min and max of the 5 numbers.")
numbers = []
for i in range(5):
    i += 1
    num = int(input('Give me number nr.: %s: (e. g.: 5)' % i))
    numbers.append(num)

min = 9999999
max = -99999
for i in numbers:
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)


# Roman numerals
def roman_to_int(s):
    print("Roman numerals to regular numbers (Dictionary version).")
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            # print('key: %s' % s)
            # print('current value: %s' % rom_val[s[i]])
            # print('if current value larger then the one before subtract '
            #       '2*"previous_value" (to remove the values from the higher '
            #       'order and itself): %s' %rom_val[s[i - 1]]
            #       )
            # print('integer value: %s' % int_val)
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            # print('integer after figuring the previous key e. g.: IV: %s' % int_val)
        else:
            int_val += rom_val[s[i]]
    return int_val


print(roman_to_int('IV'))
print(roman_to_int('MMMCMLXXXIV'))
print(roman_to_int('MMMM'))
print(roman_to_int('C'))


# Power Dictionary
def power_dictionary(n):
    power_dict = {}
    for i in range(n):
        i += 1
        power_dict[i] = pow(i, 2)
    return power_dict


print("Power 2 of range of numbers.")
print(power_dictionary(7))

# Sort by numbers/alphabet
print('Simple sorting')
print(sorted(['k', 'q', 'a']))

# Even stuff or uneven depends
some_list = [1, 2, 3, 4, 5, 6]
even_list = []
for i in some_list:
    if (i % 2) == 0:
        even_list.append(i)
print('Get just even numbers (for not even use != instead of ==)')
print(even_list)


# Fibonacci seq
def get_fibo_magic(n):
    a = 0
    b = 1
    if n == 0:
        return [0]
    elif n == 1:
        return[0, 1, 1]
    else:
        fibo_list = []
        for i in range(n):
            # b itself is the previous value
            # a + b is the new value as it gets its old self and itself
            a, b = b, a + b
            fibo_list.append(a)
        return fibo_list


print("Fibonacci seq, for a range, store i-1 value and current value 'i'"
      " and then add then to get next result, iterate (special case for 0 and 1)"
      )
print(get_fibo_magic(8))
