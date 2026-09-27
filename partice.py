# class Basket:
#     def __init__(self, location):
#         self.location = location
#         self.oranges = []
    
#     def add_orange(self, orange):
#         self.oranges.append(orange)
        
#     def sell(self , customer_name):
#         print(f"Basket at {self.location} was sold to {customer_name}.")

#     def discard(self):
#         self.oranges.clear()
#         print(f"Spoiled oranges in the basket at {self.location} were discarded.")


# class Barrel:
#     def __init__(self, size):
#         self.size = size
#         self.apples = []

#     def add_apples(self, apple):
#         self.apples.append(apple)
    

# class Orange:
#     def __init__(self, weight, orchard, date_picked):
#         self.weight = weight
#         self.orchard = orchard
#         self.date_picked = date_picked
#         self.basket = None

#     def pick(self, basket):
#         self.basket = basket
#         basket.add_orange(self)

#     def squeeze(self):
#         juice_amount = self.weight * 0.5  # Assuming 50% of the weight is juice
#         print(f"Squeezed {juice_amount} units of juice from the orange picked from {self.orchard} on {self.date_picked}.")
#         return juice_amount

# class Apple:
#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight
#         self.barrel = None
    
#     def pick(self, barrel):
#         self.barrel = barrel
#         barrel.add_apples(self)


# # _name_ "_main_" it can,t excute code first 
# if __name__ == "__main__":
#     basket = Basket("Secation A")
#     barrel = Barrel(50)

#     orange1 = Orange(200.0, "Orchard A", "2026-09-10")
#     orange2 = Orange(250.0, "Orchard B", "2026-09-11")

#     apple1 = Apple("Red", 150.0)
#     apple2 = Apple("Green", 180.0)

#     orange1.pick(basket)
#     orange2.pick(basket)

#     apple1.pick(barrel)
#     apple2.pick(barrel)

#     orange1.squeeze()

#     print("Number of oranges in basket:", len(basket.oranges))
#     print("Number of apples in barrel:", len(barrel.apples))

# Partice #1

# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age


# s1 = Student("Alice", 20)
# print(s1.name)  # Output: Alice
# print(s1.age)   # Output: 20


#2 

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         print(f"Car Brand: {self.brand}, Model: {self.model}")

# c1 = Car("Toyota", "Corolla")
# c1.show_info()  # Output: Car Brand: Toyota, Model: Corolla
        


# Partice #3
# class Mobile:
#     def __init__(self, name , price):
#         self.name = name
#         self.price = price


# m1  = Mobile("Samsung", 50000)
# m2  = Mobile("Apple", 10000)
# # print(m1.price)

#4

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, balance):
#         self.balance += balance
#         return balance
        

# b1 = BankAccount("Ali", int(500))
# print(f"Owner name: {b1.owner}")
# print(f"Initial balance: {b1.balance}")
# print(f"Deposit: {b1.deposit(300)} ")
# print(f"Total Balnace {b1.balance}")


#5 

# class Rectangle:
#     def __init__(self , length , width):
#         self.length = length
#         self.width = width

#     def area(self):
#         area = self.length * self.width
#         return area

# re = Rectangle(2, 6)
# print(f"area: {re.area()}")

# class Student:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     def add_marks(self, marks):
#         print(f"After adding {marks} Marks")
#         self.marks += marks
#         return self.marks

#     def show_result(self):
#        name = self.name
#        mark = self.marks
#        return name , mark

# s1 = Student("Ali", 50)
# print(f"Name: {s1.name}")
# print(f"Initial Marks: {s1.marks}")
# # print(f"")
# print(f"Name: {s1.name}\nTotal Marks: {s1.add_marks(20)}")



# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Ali", 20)
# print(s1.name, s1.age)
# # print(s1.age)

# class Student:
#     def __init__(self, name , mark):
#         self.name = name
#         self.mark = mark

#     def add_mark(self, mark):
#         self.mark += mark
#         return mark

# s1 = Student("Pathan", 30)
# print("Name",s1.name)
# print("Sari marks ea",s1.mark)
# s1.add_mark(20)
# print("TOtal marks", s1.mark)

#2

# class Mobile:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery


#     def charge(self, increases):
#        if self.battery + increases > 100:
#         return "Battery cannot be above 100"
#        else:
#         self.battery += increases

#     def use(self, decreases):
#         if self.battery - decreases < 0:
#             return "Battery cannot be below 0"
#         else:
#            self.battery -= decreases
#         # return self.battery

# mob = Mobile("samsung" , 50)
# print(mob.brand, mob.battery)
# mob.charge(90)
# mob.use(20)
# print(mob.battery)


#
# class Student:
#     # constructor
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age


# s1 = Student("Ali", 20)
# print(s1.name)
# print(s1.age)

# class Student:
#     def __init__(self, name , age , mark):
#         self.name = name
#         self.age = age
#         self.mark = mark

#     def add_marks(self, mark):
#         self.mark += mark
#         return self.mark

# s1 = Student("Ali", 20, 90.5)
# print(s1.name, s1.age, s1.mark)
# print(s1.add_marks(60))
# # print(s1.name, s1.age, s1.mark)


# class Student:
#     def __init__(self,name,age,mark):
#         self.name=name 
#         self.age=age
#         self.mark=mark


# s1=Student("Ali",20,50)
# print(s1.name,s1.age,s1.mark)        

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         return print(f"deposited money {self.balance}")
    
#     def withdraw(self,amount):
#         if self.balance < amount:
#             return print("Insufficient balance")
#         self.balance -= amount   
#         return print(f"withdraw money {self.balance}") 

# account1 = BankAccount("sarperaz", 20000)
# print(account1.owner,account1.balance)
# account1.deposit(10000)
# account1.withdraw(15000)

# class Car:
#     def __init__(self, brand, model, speed):
#         self.brand = brand
#         self.model = model
#         self.speed = speed

#     def accelerate(self, amount):
#         self.speed += amount
#         return print(f"speed is increase {self.speed} ")

#     def brake(self, amount):
#         if self.speed - amount < 0:
#             return "Car stop"
#         else:
#           self.speed -= amount
#         return print(f"speed is decreases {self.speed} ")

# c1 = Car("Toyota", "Corolla", 50)
# print(c1.brand, c1.model, c1.speed)
# c1.accelerate(30)
# c1.brake(10)


# class ShoppingCart:
#     def __init__(self, customer_name , total):
#         self.customer_name = customer_name
#         self.total = total

#     def add_item(self,price):
#         self.total += price
#         print(f"{self.total} added ")

#     def remove_item(self,price):
#         if self.total - price < 0:
#             print("No item added")
#         else:
#             self.total -= price
#             print(f"{price} Removes")

#     def show_total(self):
#         print(f"customer_name: {self.customer_name} Total_item purches {self.total}")

# shop = ShoppingCart("Sarperaz", 0)
# shop.add_item(200)
# shop.remove_item(50)
# shop.show_total()


# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

  
# s1 = Student("usama", 23)
# print(s1.name, s1.age)

        
class Student:
    def __init__(self, name ,mark, ):
        self.name = name
        self.mark = mark

    def add_mark(self, mark):
        self.mark += mark
        
        print(self.mark)
        

s1 = Student("baloch" , 90)
s1.add_mark(60)
# print(s1.name, s1.mark)