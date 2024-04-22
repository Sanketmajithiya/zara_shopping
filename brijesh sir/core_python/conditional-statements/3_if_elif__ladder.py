"""
An "if-elif-else" ladder in Python is a series of conditional statements used for more complex decision-making. It allows you to check multiple conditions in sequence and execute different blocks of code based on which condition is true. The syntax is as follows:

if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition2 is true (if condition1 is false)
elif condition3:
    # code to be executed if condition3 is true (if both condition1 and condition2 are false)
# ... you can have more elif blocks as needed
else:
    # code to be executed if none of the conditions are true

"""

x = 10

if x > 15:
    print("x is greater than 15")
elif x > 10:
    print("x is greater than 10 but not 15")
elif x > 5:
    print("x is greater than 5 but not 10")
else:
    print("x is 5 or less")
