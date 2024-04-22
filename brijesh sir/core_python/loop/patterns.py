
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 6

# for row in range(1,num):
#     for col in range(1, num):
#         print("*", end=' ')
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# num = 6

# for row in range(1,num):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()


# 1
# 12
# 123
# 1234
# 12345
# for row in range(1, 6):
#     for col in range(1, row+1):
#         print(col, end='')
#     print()


# A
# AB
# ABC
# ABCD
# ABCDE
# for row in range(1, 6):
#     for col in range(1, row+1):
#         print(chr(col+64), end='')
#     print()

# a
# ab
# abc
# abcd
# abcde
# for row in range(1, 6):
#     for col in range(1, row+1):
#         print(chr(col+96), end='')
#     print()


# abcde
# abcd
# abc
# ab
# a

# # abcde
# #  abcd
# #   abc
# #    ab
# #     a
# for row in range(1, 6):
#     for col in range(1, row):
#         print(' ', end='')
#     for col in range(1, 6-row+1):
#         print(chr(col+96), end='')
#     print()

# a
#  b
#   c
#    d
#     e
# for row in range(1, 6):
#     for col in range(1, row):
#         print(' ', end='')
#     print(chr(row+96), end='')
#     print()


#     a
#    b
#   c
#  d
# e
# for row in range(1, 6):
#     for col in range(1, 6-row+1):
#         if col < 6-row:
#             print(' ', end='')
#         else:
#             print(chr(row+96), end='')
#     print()

#     a
#    b
#   c
#  d
# e

#     aa
#    b  b
#   c    c
#  d      d
# e        e
# for row in range(1, 6):
#     for col in range(1, 6-row+1):
#         if col < 6-row:
#             print(' ', end='')
#         else:
#             print(chr(row+96), end='')
#     for col in range(1, row):
#             print(' '*2, end='')
#     print(chr(row+96), end='')
#     print()


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# for row in range(1, 6):
#     for col in range(1, 6-row+1):
#         if col < 6-row:
#             print(' ', end='')
#     for col in range(1, row+1):
#         print('*', end='')
#     for col in range(1, row):
#         print('*', end='')
#     print()

# for row in range(1, 6):
#     for col in range(1, row+1):
#         print(' ', end='')
#     for col in range(1, 6-row+1):
#         if col < 6-row:
#             print('*', end='')
#     for col in range(1, 6-row-1):
#         if col < 6-row:
#             print('*', end='')
    
#     print()

num = 6
for i in range(1, num):
    print(" "*(num-i), " *"*i)