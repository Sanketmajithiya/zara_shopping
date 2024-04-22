"""
In programming, a string is a sequence of characters. In most programming languages, including Python, a string is used to represent text. A character can be a letter, a digit, a punctuation mark, or even a space.

In Python, strings are created by enclosing a sequence of characters within single (' '), double (" "), or triple (''' ''' or """ """) quotes. 

Here are some examples:
single_quoted_string = 'Hello, World!'
double_quoted_string = "Python Programming"
triple_quoted_string = '''This is a
multi-line
string.'''

single_quoted_string is enclosed in single quotes.
double_quoted_string is enclosed in double quotes.
triple_quoted_string is enclosed in triple quotes, allowing for multiline strings.


"""



# name = "ToPs TeCHnoLOGy PvT. ltD."
# print(name)
# print(len(name))
# print(type(name))

# how to access a string or their elements

code = 'python'
# print(code)

# indexing(-/+)
# print(code[0], code[-1])
# print(code[1], code[-2])
# print(code[2], code[-3])
# print(code[3], code[-4])
# print(code[4], code[-5])
# print(code[5], code[-6])

# start = 0
# end = len(code)
# while(start<end):
#     print(code[start], code[-1*(start+1)])
#     start+=1

# slicing [-/+]
# syntax : string_var[start:end:step]
alpha = "abcdefghijklmnopqrstuvwxyz"
# print(len(alpha))

# print(alpha[4:])
# print(alpha[4:13])
# print(alpha[::2])
# print(alpha[::3])

# print(alpha[-2:])
# print(alpha[-2:-5:-1])

name = "ToPs TeCHnoLOGy PvT. ltD."
# print(type(name))

# print(dir(name))
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())


# code = "XXXX XXXX XXXX XXXX"
# print(code.replace(' ', '-'))

# code = 'python'
# print(code.center(20,'*'))
# print(code.startswith("py"))
# print(code.startswith("j"))
# print(code.endswith("j"))
# print(code.endswith("n"))

# code = '    python code     '
# # print(len(code))
# print(code.strip())
# print(len(code.strip()))
# print(code.rstrip())
# print(len(code.rstrip()))
# print(code.lstrip())
# print(len(code.lstrip()))

# import string
# import re
# def get_currency_code_only(input_string):
#     # Specify special symbols as delimiters
#     special_symbols = string.punctuation

#     # Use the split() method with a custom delimiter
#     result = re.split("[" + re.escape(special_symbols) + "]", input_string)

#     # Remove empty strings from the result
#     return list(filter(None, result))[-1].strip()

   
# print(get_currency_code_only("New Zealand dollar ($, NZD)"))

# print("New Zealand dollar ($, NZD)".split(" ")[-1].split(")")[0])



# start = 0
# row_data = ''
# while(start < len(currancy)):
#     if currancy[start] == ',':
#         row_data += currancy[currancy.index(currancy[start]):]
#         print()
#     start += 1

# print(row_data.split(" ")[-1].split(")")[0])

# fname = 'brijesh'
# lname = 'gondaliya'

# print(fname + ' ' + lname)

# print(fname*3)

fname = 'jay'
lname = 'gondaliya'
price = 354.765734
page = 400

# print(f"Dear {fname} {lname}, \n\nthis mail regarding attemndance")
# print("Dear {} {}, \n\nthis mail regarding attemndance".format(fname, lname))
# print("Dear %s %s, \n\nthis mail regarding attemndance\n your book price is %.2f. \n total page is %d" % (fname, lname, price, page))