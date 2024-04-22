"""
In Python, the for loop is used to iterate over a sequence (such as a list, tuple, string, or dictionary) or any iterable object. It allows you to execute a block of code multiple times, once for each item in the sequence.

Here's a basic syntax of a for loop in Python:

for item in sequence:
    # code block to be executed for each item

"""
# for var  in "python":
    # print(var)

# for var  in "python":
#     print(var.upper())


# print(list(range(0, 11, 2)))

# for num in list(range(0, 11, 2)):
#     print(num)

# for num in range(1, 11):
#     if(num % 2 == 0):
#         print(f"Even {num}")
#     else:
#         print(f"Odd {num}")


# for ch in range(0,256):
#     print(ord(chr(ch)), chr(ch))

num = 6

for row in range(1,num):
    for col in range(1, row+1):
        print("*", end=' ')
    print()
    # break
    # print(row)

# print("a", end='')
# print("b")