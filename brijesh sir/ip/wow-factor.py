# for row in range(1, 6):
#     print(" "*(5-row), " %c" % (row+64) * row )

# for row in range(4, 0, -1):
#     print(" "*(5-row), " %c" % (row+64) * row )

num = 5
for row in range(1, num):
    print(" "*(num-1-row), " *" * row )

for row in range(num-2, 0, -1):
    print(" "*(num-1-row), " *" * row )

