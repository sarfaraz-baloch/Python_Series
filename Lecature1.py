# Basic arithmetic operations in Python

# a = 2
# b = 4
# c = a + b
# print(a - b , "addition result:")
# print(a * b , "multiplication result:")
# print(a / b, "division result:")    
# print(a % b , "modulus result:")
# print(a ** b , "exponentiation result:")
# print(a // b , "floor division result:") 


# realtional operators in Python

# a = 50
# b = 20
# print(a > b , "greater than result:")
# print(a < b , "less than result:")
# print(a == b , "equal to result:")
# print(a != b , "not equal to result:")
# print(a >= b , "greater than or equal to result:")
# print(a <= b , "less than or equal to result:")

# Assignment operators in Python

# x = 10
# x += 10
# print(x , "after += operator:")

# y = 20
# y -= 10
# print(y , "after -= operator:")

# z = 5
# z *= 2
# print(z , "after *= operator:")

# a = 15
# a /= 3
# print(a , "after /= operator:")

# b = 25
# b %= 4
# print(b , "after %= operator:")

# c = 7
# c **= 2
# print(c , "after **= operator:")

# num = 10 
# num **= 5
# print(num, "after **= operator:")

# d = 22
# d //= 5
# print(d , "after //= operator:")

# Logical operators in Python

# NOT operator  

# print(not True , "not operator result:")
# print(not False , "not operator result:")

# AND operator

# val1 = True
# val2 = True
# print(val1 and val2 , "and operator result:")

# val3 = 50
# val4 = 60
# print ( (50==60) or (val3 < val4) , "or operator result:")


#  how to take input from user in python
# input always takes input in string format

# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# age = int(input("Enter your age: "))
# print("You are " + str(age) + " years old.")
# The int() function is used to convert the input string to an integer.

# age = float(input("Enter your price: "))
# print("The price is " + str(age) + ".")
# The float() function is used to convert the input string to a float.

# value1 = int(input("Enter first number: "))
# value2 = int(input("Enter second number: "))
# print("Sum:", value1 + value2)

# partice questions



# # 1
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("Product:", a * b)

# # 2
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("Remainder:", a - b)

# 3

# a = int(input("Enter a number: "))
# b = int ((input("Enter another number: ")))
# print("Quotient:", a / b)

# 4
# a= 7
# b= 3
# print("Remainder:", a % b)
# print("Exponent:", a ** b)
# print("==>:", a // b)

# 5
# a = int(input("Enter a number: "))
# b = a ** a
# print("Exponent:", b)

# 5
# a = 40
# b = 15
# print("Is a greater than b?", a > b)
# print("Is a less than b?", a < b)
# print("Is a equal to b?", a == b)

# 6
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# print( x > y )
# # print( x == y )

# 7
# x = 5
# x += x + 5
# print(x)  # Output: 10

# 8
y = 20
y //= 3
# print(y)  # Output: 4

# 9
num = 4
num **= num
# print(num)  # Output: 256

# 10
# print(not (10 > 5))
c = 10
d = 20
# print((c > d) and (c == d)) # Output: False
# print((c < d) or (c == d))  # Output: True

# 11
# Output: True

# user_number1 = int(input("Enter the first number: "))
# user_number2 = int(input("Enter the second number: "))
# print_sum = user_number1 + user_number2
# print("The sum of user1", user_number1, "and the user2", user_number2, "is:", print_sum)

# 12

# user_num1 = int(input("Enter the first number: "))
# result = user_num1 / 2
# print("Half of", user_num1, "is:", result)

# 13

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print("Hello", user_name, ", you are", user_age, "years old.")

# 14

user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))
print((user_num1 > user_num2 , user_num1 ) and (user_num2 < user_num1 , user_num2))