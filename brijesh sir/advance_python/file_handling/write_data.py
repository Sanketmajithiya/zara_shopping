file = open('sample.txt', 'w')
lines = ['This is a line 1\n', 'This is a line 2\n', 'This is a line 3\n', 'This is a line 4\n', 'This is a line 5']
# file.write("This is a c code.")
file.writelines(lines)
file.close()