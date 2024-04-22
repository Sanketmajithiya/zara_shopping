"""
List - ordered, mutable, indexing, slicing, duplicate values are  allowed

In Python, a list is a data structure that is used to store a collection of items. It is an ordered and mutable (changeable) collection of objects, meaning you can add, remove, or modify elements after the list has been created. Lists are created by placing a comma-separated sequence of items within square brackets [ ] or using list().

syntax : 
list_name = []
list_name = list()
"""

# list_name = [1,'hghfyh', 67.09, 2, 4]
# print(list_name)
# print(len(list_name))
# print(type(list_name))

m_items = ['milk', 'butter-milk', 'potato']
n_items = ['milk', 'tomato']
a_items = ['drink', 'chocolate']

total_items = m_items + n_items + a_items

# access a list items
#--------------------

# print(total_items)

# indexing (-/+)
# print(total_items[4])
# print(total_items[4])
# print(total_items[5])
# print(total_items[4])

# print(total_items[-3])
# print(total_items[-3])
# print(total_items[-3])
# print(total_items[-4])

# ['milk', 'butter-milk', 'potato', 'milk', 'tomato', 'drink', 'chocolate']
# print(total_items[0:3])
# print(total_items[3:5])
# print(total_items[-2::-1])
# print(total_items[5:7:1])
# print(total_items[3:])

# empty_list = []
# for item in total_items:
#     if item not in empty_list:
#         empty_list.append(item)
#         print(item.title(), f"{total_items.count(item)}")


vegs = ['tomato', 'patato', 'onion']
# print(dir(vegs))


# add
# # 'append', 'extend', 'insert'
# new_vegs = ['cabbage', 'garlic']
new_vegs = 'chilli'
# vegs.extend(new_vegs)
# vegs.append(new_vegs)
# vegs.insert(0, new_vegs)
# vegs.insert(1, new_vegs)


# print(vegs)
# update
# vegs[1] = new_vegs
# print(vegs)

# delete
# 'clear', 'pop', 'remove',
# vegs.clear()
# vegs.pop()
# vegs.remove('1')
# vegs.remove('patato')


# del vegs[0]
# print(vegs)

# mix
# 'copy', 'count', 'index','reverse', 'sort'

# v = vegs.copy()
# print(id(v))
# print(id(vegs))

# x  = 10
# y = x
# print(id(x))
# print(id(y))

# print(vegs.index('patato'))

# vegs.reverse()
# vegs.sort()
# print(vegs)

# nums = [1,2,3].append(4)
# print(nums)

# name = "pyThon".lower()
# print(name)