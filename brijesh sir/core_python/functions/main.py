"""

In Python, a function is a block of reusable code that performs a specific task. Functions allow you to organize your code into logical blocks, making it easier to read, understand, and maintain. Functions in Python are defined using the def keyword followed by the function name, parentheses (), and a colon :. Here's a basic syntax of a function in Python:

def function_name(parameters):
    # function body
    # code to perform the task
    return value # optional


In Python, a function is a block of reusable code that performs a specific task. Functions allow you to organize your code into logical blocks, making it easier to read, understand, and maintain. Functions in Python are defined using the def keyword followed by the function name, parentheses (), and a colon :. Here's a basic syntax of a function in Python:

python
Copy code
def function_name(parameters):
    # function body
    # code to perform the task
    return value # optional

function_name(parameters)
Let's break down the components of a function:

def: This keyword is used to define a function.
function_name: This is the identifier of the function. It should follow the same naming conventions as variables.
parameters: These are optional. They are values that can be passed into the function when it is called. Functions can accept zero or more parameters.
function body: This is the block of code inside the function that performs the specific task. It can contain any valid Python code.
return: This keyword is used to return a value from the function. It is optional, and a function may not have a return statement. If included, it can return zero or more values.
"""

# def add(a, b=20):
#     print(a + b)

# def add(a, b=20):
#     return a + b, a*b

# print(add(10, b=50))
# print(add(10, 30)[0])

# positional para
# def fullname(fname, lname):
#     print(fname + ' ' + lname)

# fullname('brijesh', 'gondaliya')

# default para
# def fullname(fname, lname="patel"):
#     print(fname + ' ' + lname)

# fullname('brijesh', 'gondaliya')


# keyword para
# def fullname(fname='brijesh', lname="patel"):
#     print(fname + ' ' + lname)

# fullname()


# variable length para
# *args, **kwargs

# def add(*nums):
#     sum = 0
#     for num in nums:
#         sum += num
#     print(sum)

# add(10,20,30,40,50, 100)

# def bill(**products):
#     total_amount = 0
#     for k, v in products.items():
#         total_amount += v
#         print(k, v)
#     print( total_amount)

# bill(tomato=20, potato=30, book=20, pen=100)


# x = 10 # global var

# def test():
    
#     print(x)
#     x = 20 # local var
#     # print(x) 

# test()
# print(x)

# code = lambda x, y, z:x * y + z
# print(code(10,20, 30))