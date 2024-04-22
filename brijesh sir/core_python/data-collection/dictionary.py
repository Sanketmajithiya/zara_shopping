"""
Dictionary : mutable, unordered, Unindexed, duplicate keys are not allowed 
In Python, a dictionary is a built-in data type that stores key-value pairs. It is mutable, meaning you can modify its contents after creation. Dictionaries are unordered collections, which means that the order in which items are stored doesn't necessarily reflect the order in which they were added.

syntax :

dict_name = {
    'key1':'value1',
    'key2':'value2'
}

dict_name = dict()
"""

store = {
    'vegs':{
        'tomato':{
            'price-p/kg':30,
            'qty':'20k'
        },
        'potato':{
            'price-p/kg':20,
            'qty':'100k'
        }
    },
    'fruites':{
        'apple':{
            'price-p/kg':100,
            'qty':'50k'
        },
        'banana':{
            'price-p/dozen':24,
            'qty':'30dozen'
        }
    }
}

# print(len(store))
# print(type(store))


# print(dir(store))

# 'clear', 'copy', 

# 'get', 'keys', 'values', 'items'
# Accessing values
# print(store['vegs'])
# print(store.keys())
# for key in store.keys():
#     print(key)

# print(store.values())
# for value in store.values():
#     print(value)

# print(store.items())
# for var in store.items():
#     key =var[0]
#     value =var[1]
#     print(key, value)
    # break

# print(store.get('vegs'))

# Modifying values
# store['vegs'] = '5vegs'


#  'update'
# Adding new key-value pairs
# store['drinks'] = 'coco'
# store.update({
#     'new-fruites':{
#         'guava':{
#             'qty':'20k'
#         }
#     }
# })
# print(store)



# 'pop', 'popitem',
# Removing key-value pairs
# del store['vegs']

# store.pop('vegs')
# store.popitem()
# print(store)


# a = 10
# a = 30


# 'fromkeys',   

# book_list = ['python', 'java', 'php']
# price = 20
# books = dict()
# # print(books.fromkeys(book_list, price))
# books.fromkeys(book_list, price)
# print(books)


# car = {
#     'color':'black',
#     'name':"BMW"
# }

# car.setdefault('model', "sghdjh@##d")
# car.setdefault('color', "red")
# print(car)

for i in ['cfjkgb','kjfchgdu', 'mhdgfh']:
    print(i)