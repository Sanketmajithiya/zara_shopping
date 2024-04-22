"""
In Python, operators are special symbols or keywords that perform operations on operands. Here are the main types of operators in Python:

Example : 
x = 10
y = 20

z = x + y

here
 + is operator & 
 z, x and y is a operands

Arithmetic Operators:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus - returns the remainder of a division)
// (Floor Division - returns the quotient with rounding down)
x = 10
y = 2
print(x//y)

** (Exponentiation)
print(2**5)



Assignment Operators:

= (Assignment)
+= (Addition assignment)
-= (Subtraction assignment)
*= (Multiplication assignment)
/= (Division assignment)
%= (Modulus assignment)
//= (Floor division assignment)
**= (Exponentiation assignment)

x = 10
# x = x + 5
x += 5
print(x)


Comparison (Relational) Operators:

== (Equal to)
!= (Not equal to)
< (Less than)
> (Greater than)
<= (Less than or equal to)
>= (Greater than or equal to)

x = 1
y = 0
a = True
b = False


# print(a == x)
# print(b != y)

# print(((y < x) != (x)) < (y + a))
# print(((y < x) != (x)) < (1))
# print(((1) != (x)) < (1))
# print((0) < (1))
# print(True)

Logical Operators:

and (Logical AND)
or (Logical OR)
not (Logical NOT)

A B C ... and   or 
T T T     True  True
F T T     False True
T F T     False True
T T F     False True
F F F     False False

T not False
F not True


A = 0 < 34
B = True
C = False

# print(A and B and C)
print(A and C or B)


Membership Operators:

in (True if a value is found in the sequence)
not in (True if a value is not found in the sequence)

name = "brijesh"

print('p' in name)
print('p' not in name)
print('rij' not in name)
print('rij' in name)

Bitwise Operators:

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
~ (Bitwise NOT)
<< (Left shift)
>> (Right shift)

5 & 3
0101
0011
=====
0001


A B & | ^ ~
0 0 0 0 0 1
1 0 0 1 1 0
0 1 0 1 1 1
1 1 1 1 0 0


# print(5 & 3)
# print(5 | 3)
# print(5 ^ 3)
# print(~ 5)

x = 7
x = x<<1 # 14
x = x<<3
print(x)


"""

