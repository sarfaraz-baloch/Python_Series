# #  Lecature 3 

# # listeds in Python
# # A listed is a collection which is ordered and changeable. In Python, listeds are written with square brackets  
# # listed are used to store multiple items in a single variable and its mutable.

# # 1

# fruits = ["apple", "banana", "cherry"]

# # print(fruits)
# fruits[1] = "blackcurrant"  # Change the second item
# # print(fruits)

# # 2
# # Methods to manipulate listeds

# listed_6 = [1, 2, 3, 4, 5]
# # append()	Adds an item to the end of the listed
# listed_6.append(6)  # Add an item to the end of the listed 
# # print(listed)

# # Sort ()
# numbers = [4, 2, 9, 1, 5, 6]
# numbers.sort()  # Sort the listed in ascending order
# numbers.sort( reverse=True) # Sort the listed in descending order
# # print(numbers)

# # reverse()	Reverses the order of the listed
# # reverse()
# number= [4, 2, 9, 1, 5, 6]
# number.reverse()  # Reverse the order of the listed
# # print(number)

# # insert()	Inserts an item at the specified index
# # insert()
# colors = ["red", "green", "blue"]
# colors.insert(0, "yellow")  # Insert "yellow" at index 1
# # print(colors)

# # remove()	Removes the first item with the specified value
# # remove()
# animals = ["cat", "dog", "rabbit", "dog"]
# animals.remove("dog")  # Remove the first occurrence of "dog"
# # print(animals)

# # pop()	Removes the item at the specified index, or the last item if index is not specified
# # pop()

# cities = ["New York", "Los Angeles", "Chicago", "Houston"]
# popped_city = cities.pop(3)  # Remove the item at index 3
# # print(popped_city)    
# # print(cities)

# # Tuple in Python
# # A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.
# # Tuples are used to store multiple items in a single variable and its immutable.
# # 1
# thistuple = ("apple", "banana", "cherry")
# # print(thistuple)
# # thistuple[1] = "blackcurrant"  # This will raise an error because tuples are immutable
# # print(thistuple)

# # 2
# # Methods to manipulate tuples
# # count()	Returns the number of times a specified value occurs in a tuple
# # index()	Searches the tuple for a specified value and returns the position of where it
# # count()

# tup = (1, 2, 3, 2, 4, 2)
# x = tup.count(2)  # Count the occurrences of 2 in the tuple

# tup2 = (1, 2, 3, 4, 5)
# y = tup2.index(1)  # Find the index of the first occurrence of 1 in the tuple
# # print(x)
# # print(y)

# # Partice exercises:
# # 1. Create a listed of your favorite movies and add a new movie to the listed.

# # listed_of_movies = []
# # # print(listed_of_movies)
# # user1 = input("Enter your favorite movie: ")
# # listed_of_movies.append(user1)
# # user2 = input("Enter another favorite movie: ")
# # listed_of_movies.append(user2)
# # user3 = input("Enter one more favorite movie: ")
# # listed_of_movies.append(user3)
# # # print(listed_of_movies)   


# # 2
# # plandrome check

# val1 = [1, 2, 3, 2, 1]
# val2 = val1.copy()
# val2.reverse()

# # if(val1 == val2):
# #     print("The listed is a palindrome")
# # else:
# #     print("The listed is not a palindrome")   

# Grade_Sort = [ "E", "B", "f", "D", "C", "A"]
# # print("Original listed: ", Grade_Sort)

# listed_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# listed_number.append(10)
# listed_number.insert(2, 15)
# listed_number.pop(5)
# # print(listed_number)

# marks = [45, 12, 89, 32, 67]
# marks.sort()
# # print(marks)
# marks.reverse()
# # print(marks)

# numbers_count = [1, 2, 3, 2, 4, 2, 5]
# # print(numbers_count.count(2))


# subjects = ("Math", "Physics", "Chemistry", "Math", "Biology")
# print(subjects.count("Math"))
# # print(subjects.index("Chemistry"))

# input_num = [1,2,3,2,1]
# rev_num = input_num.copy()
# rev_num.reverse()
# if(input_num == rev_num):
#     print("The listed is a palindrome")
# else:
#     print("The listed is not a palindrome")


# num = (10, 20, 30, 40, 50, 20, 60)
# # print(num.count(20))
# # print(num.index(40))


# colors = ["red", "green", "blue"]
# colors.append("yellow")
# coverted_tuple = tuple(colors)
# # print(coverted_tuple) 

# my_tuple = (10, 20, 30, 40, 50)

# # Convert tuple to listed
# my_listed = list(my_tuple)
# changed_list = my_listed.insert(2, 99)
# # Convert listed back to tuple
# new_tuple = tuple(my_listed)
# # print(new_tuple)

# # end of lecature3.py



# Partive exercises:

# Fruits = ["apple", "banana", "cherry"]
# Fruits.insert(1, "orange")
# Fruits.remove("banana")
# # print(Fruits)

# nums = [10, 20, 30, 40]
# nums[2] = 35
# print(nums)

# empty_list = []
# input1 = int(input("Enter first Number: "))
# input2 = int(input("Enter second Number: "))
# input3 = int(input("Enter third Number: "))
# empty_list.append(input1)
# empty_list.append(input2)
# empty_list.append(input3)
# print(empty_list)

numbers = [5, 1, 4, 2, 3]
numbers.sort()
numbers.reverse()
# print(numbers)

# colors = ["red", "green", "blue"]
# colors.reverse()
# print(colors)

# colors = ["red", "green", "blue"]
# colors.insert(1, "yellow")
# print(colors)

# animals = ["cat", "dog", "rabbit", "dog"]
# animals.remove("dog")
# print(animals)

# cities = ["Karachi", "Lahore", "Quetta", "Islamabad"]
# popped_city = cities.pop(2)
# print(popped_city)

# data = [1, 2, 3, 2, 1]
# reversed_data = data.copy()

# if(data == reversed_data):
#     print("The listed is a palindrome")
# else:
#     print("The listed is not a palindrome")

# nums = [1, 2, 3, 4, 5]
# nums.append(10)
# nums.insert(3,99)
# nums.remove(4)
# print(nums)

# marks = [45, 12, 89, 32, 67]
# marks.sort()
# marks.reverse()
# print(marks)

# nums = [1, 2, 3, 2, 4, 2, 5]
# print(nums.count(2))

# subject = ("Math", "Physics", "Chemistry", "Math", "Biology")
# print(subject.index("Chemistry"))
# print(subject.count("Math"))


# nums = (10, 20, 30, 40, 50, 20, 60)
# converted_list = list(nums)
# converted_list.insert(2, 99)
# print(converted_list)
# colors = ["red", "green", "blue", "yellow"]
# converted_list_from_colors = tuple(colors)
# print(converted_list_from_colors)

nums = [1, 2, 3, 2, 1]
reversed_nums = nums.copy()
if(nums == reversed_nums):
    print("The listed is a palindrome")
else:
    print("The listed is not a palindrome")