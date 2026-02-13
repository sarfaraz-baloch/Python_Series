# Lecature 4
# Dictionaries and Sets in Python
# dictoonaries are used to store data values in key:value pairs.
# they are unordered, mutable(can be changed), and don't allow duplicate keys.

info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

info["age"] = 31  # updating age
info["profession"] = "Engineer"  # adding new key-value pair

# print(info)

# 1 empty dictionary
empty_dict = {}
empty_dict['phone'] = '123-456-7890'
empty_dict['email'] = 'zVw0g@example.com'
# print(empty_dict)

# 2 another way to create a dictionary
another_dict = dict()
another_dict["fruit"] = "Apple"
another_dict["quantity"] = 5
another_dict["price"] = 0.99
# print(another_dict)

# nested dictionary
student = {
 "name" : "sarfi",
    "marks" : {
        "math" : 90,
        "science" : 85
    }
}

# print(student)  # accessing nested dictionary value

# methods in dictionary
# keys()	Returns a list of all the keys in the dictionary
# values()	Returns a list of all the values in the dictionary
# items()	Returns a list of all the key-value pairs in the dictionary
# get() Returns the value of the specified key
# update() Updates the dictionary with the specified key-value pairs

# print(student.keys())
# print(student.values())
# print(student.items())
# # print(student["name2"]) # accessing value using key but if key is not present it will give error
# print(student.get("name")) # accessing value using get method if key is not present it will return None
# print(student.get("name2", "Not Found")) # accessing value using get method with default value
# student.update({"age": 20})  # adding new key-value pair using update method
# my_dict = {"city": "Los Angeles"}
# student.update(my_dict)  # updating existing key-value
# print(student)


# Sets in Python
# we cant add list and dictionary in set because they are mutable but we can add tuple because it is immutable.
# sets are unordered collections of unique elements.
# they are mutable(can be changed) but do not allow duplicate elements.
#  we use set in corlebrais {} to create a set
# we can just add immutable elements in a set.
# 1 add ()
# 2 remove()
# 3 clear()
# 4 pop()
# union()
# intersection()

my_set = {1, 2, 3, 4, 5}
my_set2 = {1, 2, 3, 4, 5, 2 , 3}  # duplicate elements will be ignored 
my_set3 = {"a", "b", "c"  , "a"}  # duplicate elements will be ignored

collection = set()
collection.add(10)
collection.add(20)
collection.add(10)  # duplicate element will be ignored
collection.remove(20)
collection.add((1, 2))  # adding tuple
# print('collection',collection)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# union
set_union = set1.union(set2)
# intersection
set_intersection = set1.intersection(set2)
# print('set_union',set_union)
# print('set_intersection',set_intersection)



# user_dict = {}
# input1 = input('enter your name: ')
# user_dict.update({'name': input1})
# input2 = input('enter your age: ')
# user_dict.update({'age': input2})
# input3 = input('enter your city: ')
# user_dict.update({'city': input3})
# print(user_dict)

# possible ways to create a set with single element like 9 and 9.0 same value but different data types
marks = {(int(9) , float(9.0)),}
marks2 = {(9, 9.0),}
print(marks)
print(marks2)




























# Partice exercises:

person = {
    "name": 'John',
    "age": '20',
    "city": 'New York'
}
# print(person)

info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

info.update({"age": 31})  # updating age
# print(info)


empty_dict = {}
empty_dict['phone'] = '123-456-7890'
empty_dict['email'] = 'zVw0g@example.com'
# print(empty_dict)

my_dict = dict()
my_dict["fruit"] = "Apple"
my_dict["quantity"] = 5
my_dict["price"] = 0.99
# print(my_dict)

student_info = {
    "name": 'john',
    'math':{
        'marks': 90
    }
}

# print(student_info)
# print(student_info.items())
# print(student_info.keys())
# print(student_info.values())


student_info.get("name") 
student_info.get("name2", "Not Found")

# print(student_info.get("name"))
# print(student_info.get("name2", "Not Found"))

student_info.update({"age": 20})
my_dict = {"city": "Los Angeles"}
student_info.update(my_dict)
# print(student_info)

my_num = {1, 2, 3, 4, 5}
depulited_num = {1, 2, 3, 4, 5, 2, 3} # set ignore duplicates values and return unique values

# print(my_num)
# print(depulited_num)
alphabet_set = {"a", "b", "c", "a"}
# print(alphabet_set)

# Difference between List and Dictionary:
# 1 in List elements are ordered, in Dictionary elements are unordered key-value pairs.
# 2 List allows duplicate elements, Dictionary does not allow duplicate keys.
# 3 List is accessed using index, Dictionary is accessed using keys.
# 4 List is defined using square brackets [], Dictionary is defined using curly braces {}.
# 5 List is mutable(can be changed), Dictionary is also mutable(can be changed).
# 6 List is used to store multiple items in a single variable, Dictionary is used to store data values in key:value pairs.

# Difference between Set and Dictionary:
# 1 Set is an unordered collection of unique elements, Dictionary is an unordered collection of key-value pairs.
# 2 Set does not allow duplicate elements, Dictionary does not allow duplicate keys.

# 15 True or False:
# 1 A dictionary is an ordered collection of key-value pairs. True
#  Sets allow duplicate elements : False
#  3 Dictionaries are mutable : True
