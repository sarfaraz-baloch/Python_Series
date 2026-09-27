# static method

# class Student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark

#     @staticmethod
#     def welcome():
        
#         print("Hello user")

# s1= Student("Ali", 50)
# print(s1.name, s1.mark)
# s1.welcome()


# class Student:
#     def _init_(self,name,mark):
#         self.name=name
#         self.mark=mark

#     @staticmethod
#     def welcome():
#      print("hello sister")


# s1=Student("name", 90)
# s1.welcome()

# class Student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

    
#     def add_mark(self, mark):
#      self.mark += mark
     
#     @staticmethod
#     def hello():
       
#        print("Hello user")

     

# s1 = Student("Ali" ,70)
# s1.add_mark(80)
# print(s1.mark)
        
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def show_info(self):
#         print(self.name, self.age)

# s1 = Student("Ali", 20)
# print(s1.name)


# Single intertince
# Multiple Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car is started")

#     @staticmethod
#     def stop():
#         print("Stop")

# class BMW(Car):
#     def __init__(self, name):
#         self.name = name

# c1 = BMW("BMW")
# print(c1.name)
# c1.start()



# multi_level interitance 
# class Father:
#     def face(self):
#         print("Face shap")

# class Mother:
#     def fat(self):
#         print("zandi")

# class Child(Father, Mother):
#     def __init__(self, name):
#         self.name = name

# c1 = Child("Ali")
# c1.face()
# c1.fat()
# print(c1.name)

# class Bank_account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = amount

#     def show_balance(self):
#         print("Balance", self.balance)

# class SavingsAccount(Bank_account):
#     # def __init__(self, interest):
#     #     self.interest = interest

#     def add_interest(self, interest):
#         self.balance += self.balance * interest / 100
#     @staticmethod
#     def minimum_balance(balance):
#         if balance >= 10000:
#             print("Valid")
#         else:
#             print ("Low Balance")

# account = SavingsAccount("Ali" , 1000)
# print(f"Name: {account.owner}")
# account.deposit(10000)
# # interest formula = balance * interest / 100
# account.add_interest(5)
# account.show_balance()
# account.minimum_balance(account.balance)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print(f"Name: {self.name} Age: {self.age}")

# class Student(Person):
#     def __init__(self,name , age, id):
#         super().__init__(name, age)
#         self.id = id
#         self.marks = []

#     def add_marks(self, marks):
#         self.marks.extend(marks)

#     def calculate_average(self):
#         total = sum(self.marks)
#         average = total / len(self.marks)
#         return average
#     def show_student(self):
#         print(f"Name: {self.name}\nage: {self.age}\nid: {self.id}\nMarks: {self.marks}\nScholarship_Amount: {self.scholarship_amount}")

#     @staticmethod
#     def check_result(average):       
#       if average >= 80 :
#             print("Grade A")
#       elif average >= 70 :
#           print("Grade B")
#       elif average >= 60:
#           print("Grade C")
#       else:
#           print("Fail")

# class ScholarshipStudent(Student):
#     def __init__(self, name, age, id, scholarship_amount):
#         super().__init__(name, age, id)
#         self.scholarship_amount = scholarship_amount

#     def add_scholarship(self,amount):
#         self.scholarship_amount += amount

#     def show_scholarship(self):
#         # override the show_student method
#         super().show_student()
#         print(f"Amount: {self.scholarship_amount}")

    

# student = ScholarshipStudent("Ali", 20, "1113280", 5000)
# student.add_marks([22, 77, 90])
# student.show_student()
# average = student.calculate_average()
# student.check_result(average)

# s1 = Student("Ali", 20, 1120)
# s1.show_person()
# s1.add_marks([37, 79 , 89, 89])
# # print(s1.calculate_average())
# s1.show_student()
# s1.check_result(s1.calculate_average())


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance: ", self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self, interest):
        self.balance += self.balance * interest / 100 
        print("After adding interest", self.balance)

account = SavingsAccount("Ali" , 9000)

print(account.owner, account.balance)
account.deposit(1000)
account.show_balance()
account.add_interest(5)

