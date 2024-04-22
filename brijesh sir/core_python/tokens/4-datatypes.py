"""
In programming, data types are a classification or categorization of data items. They represent the kind of values that variables can hold and the operations that can be performed on those values. Different programming languages support various data types, and each data type has its own set of rules and operations.

Numeric Types:

int: Integer type (whole numbers). (N(-1)/P(1))
float: Floating-point type (decimal numbers). (N(-1.0)/P(1.0))
complex: Complex numbers with real and imaginary parts.(30 + 45j)

Example :
    age = 27, page = 300
    price = 41.50
    complex = 20 + (-2)j

Text Type:

str: String type, used for representing sequences of characters (text).

Example : 
    name = 'oyo'
    name = "oyo"
    name = '''oyo'''
    name = \"\"\"oyo\"\"\"

Boolean Type:

bool: Boolean type, representing either True or False values.

Example :
    is_active = True
    is_super_admin = False

Sequence Types:

    list: List type, ordered and mutable sequence of elements.
    tuple: Tuple type, ordered and immutable sequence of elements.
    range: Represents a sequence of numbers.

Mapping Type:

dict: Dictionary type, an unordered collection of key-value pairs.

Set Types:

set: Set type, an unordered collection of unique elements.
frozenset: Immutable set.

None Type:

NoneType: Represents the absence of a value or a null value.

Binary Types:

bytes: Represents a sequence of bytes.
bytearray: Mutable version of bytes.
memoryview: Provides a view on a memory block.
"""
# int_num = 20

# print(type(int_num))

# boolen_value = isinstance(int_num, float)

# print(type(boolen_value))

# print(boolen_value)


"""
In Python, variables can have implicit or explicit data types, and the language itself is dynamically typed. This means that you don't need to declare the data type of a variable explicitly, and the interpreter determines the type based on the assigned value. However, you can also explicitly specify the data type if needed.
Implicit Data Types:
Dynamic Typing:

Python is dynamically typed, which means you can change the type of a variable at runtime.

Example of implicit data type:
x = 5
x = "jk"
print(type(x))



Explicit Data Types:
Type Casting:

You can explicitly cast a variable to a specific data type using casting functions such as int(), float(), str(), etc.

Example of explicit data type:
"""

x = 5
x = float(x)
x = str(x)
# print(type(x))


# x = "454"
# x = int(x)
# print(type(x))


# x = 'a'
# print(ord(x))

# x = 97
# print(chr(x))