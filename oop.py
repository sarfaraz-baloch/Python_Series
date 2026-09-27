# a = 10
# b = 20
# sum = a + b

# diff = a - b

# print(sum)
# print(diff)

# OOP (Object Oriented Programming) is a programming paradigm that uses objects and classes to organize code.
# It allows for the creation of reusable and modular code, making it easier to manage and maintain.

# Class is a template or blueprint for creating objects.
# It defines the properties and methods that objects of that class will have.

# Object is an instance of a class.
# It is a specific instance of a class that has its own unique attributes and methods.

# class Student:
#     name = "John"

# s1 = Student() # creating an object of the class Student
# print(s1.name) # accessing the property of the object s1

# class Car:
#     name = "BMW" # property of the class Car
#     color = "red" # property of the class Car


# print(Car.name) # accessing the property of the class Car
# print(Car.color)


# Constructor is a special method that is called when an object is created.
# It is used to initialize the properties of the object.
# It is also called initializer or constructor
#  __init__() is the constructor method in Python. 
# It is a special method that is called when an object is created.

# class Student:
#     # name = "John" # property of the class Student
#     def __init__(self, fullname , age):
#         self.age = age
#         self.name = fullname # initializing the property of the object
#         print("Constructor is called")


# s1 = Student("John", 20)
# s2 = Student("Max", 30) # creating an object of the class Student
# print(s2.name) # accessing the property of the object s2
# print(s2.age) # accessing the property of the object s2


# class Car:
#     # default constructor
#     def __init__(self):
#         pass

#     # parameterized constructor
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# c1 = Car("BMW", "red") # creating an object of the class Car
# print(c1.name) # accessing the property of the object c1
# print(c1.color) # accessing the property of the object c1

# class & intance attributes

# class Car:
#     # class attribute
#     color = "red"

#     # instance attribute
#     def __init__(self, name):
#         self.name = name

# c1 = Car("BMW") # creating an object of the class Car
# print(c1.name) # accessing the property of the object c1
# print(c1.color) # accessing the property of the object c1

# Methods
# methods are funcation that belong to objects. They are used to define the behavior of objects.
# they are defined inside classes and are called by objects.

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     # method
#     def welcome(self):
#         print("Welcome to the class " + self.name + " your marks is " + str(self.marks))
    
#     # method
#     def get_marks(self):
#         return self.marks

# s1 = student("John", 85) 
# s1.welcome() # calling the method welcome() of the object s1
# print(s1.get_marks()) # calling the method get_marks() of the object s1


# Partice questions

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i 
#         print(f"Hello {self.name} your total marks is {sum /3}")

# s1 = Student("John", [85, 90, 95])
# s1.avg()
# s1.name = "Max"
# s1.avg()


# Static Methods
# Static methods are methods that belong to a class rather than an instance of a class.


# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     # Static method are those which self parameter is not used in the method. 
#     # They are defined using the @staticmethod decorator.
#     @staticmethod
#     def welcome():
#         print("Welcome to the Car Showroom")


# c1 = Car("BMW", "red")
# c1.welcome()


# Abstraction is a process of hiding the implementation details and showing only the functionality to the user.
# Abstraction is a way of representing the real-world objects in a simplified way.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True

#         if self.acc and self.clutch == True:
#             print("Car is started")
#         else:
#             print("Car is not started")

# c1 = Car()
# c1.start()


# Encapsulation 
# Wrapping data and Funcation into a singal unit (object)



# 2. Partice

# class Account:
#     def __init__(self, balance , account_number):
#         self.balance = balance
#         self.account_number = account_number
    
#     def debit(self, ammount):
#         self.balance -= ammount
#         print(f"{ammount} is debit to your account {self.get_balance()}")
    
#     def credit(self, ammount):
#         self.balance += ammount
#         print(f"{ammount} is credit to your account {self.get_balance()}")
    
#     def get_balance(self):
        
#         return self.balance


# account1 = Account(10000, "PK12389")
# account1.debit(2000)
# account1.credit(5000)


# polymorphism is the ability of an object to take on many forms.
# inerithance is the ability of a class to inherit properties and methods from another class.

# del keyword is used to delete an object or a variable.


# class Student:
#     def __init__(self, name , age):
#         self.age = age
#         self.name = name
    
# s1 = Student("John", 20)
# print(s1.name)
# del s1
# print(s1.name) # this will give an error because the object s1 is deleted

# Private attributes and methods
# private attributes and methods are attributes and methods that are not accessible from outside the class.
# they are prefixed with double underscore "__"

# class Account:
#     def __init__(self, balance , account_number):
#         self.ba = balance
#         self.__an = account_number # private attribute cannot be accessed from outside the class

#     def get_account_number(self):
#         return self.__an # private attribute can be accessed from inside the class
    

    
# acc1 = Account(10000, "PK12389")
# print(acc1.ba)
# print(acc1.get_account_number()) # private attribute can be accessed from inside the class
# print(acc1.an)

# Inheritance
# when one class (child / derived) derives properties and methods from another class (parent / base) it is called inheritance.
# Types of inheritance:

# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance

# class Car:
#     @staticmethod
#     def start():
#      print("Car is started")

#     @staticmethod
#     def stop():
#         print("Car is stopped")

# class BMW(Car):
#    def __init__(self, name):
#        self.name = name
    
# c1 = BMW("BMW")
# print(c1.name)
# c1.start()

# Multi-level Inheritance

# class Car:
#     @staticmethod
#     def start():
#      print("Car is started")


# class BMW(Car):
#    def __init__(self, name):
#        self.name = name

# c1 = BMW("BMW")
# class BMWX5(BMW):
#    def __init__(self,type): 
#        self.type = type


# c2 = BMWX5("Petrol")
# print(c1.name)
# print(c2.type)
# c1.start()
        
# multiple inheritance is a feature of object-oriented programming languages in which a class can inherit properties and methods from more than one parent class.

# class A:
#     var1 = 10

# class B:
#     var2 = 20
    
# class C(A,B):
#     var3 = 30

# c1 = C()
# print(c1.var1)
# print(c1.var2)
# print(c1.var3)


# Super method
#  is a method that is used to call the parent class constructor from the child class constructor.

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car is started")
    

# class BMW(Car):
#     def __init__(self, name, type):
#         super().__init__(type) # calling the parent class constructor from the child class constructor
#         self.name = name
#         super().start() # calling the parent class constructor from the child class constructor

# c1 = BMW("BMW", "Petrol")
# print(c1.type)
        

