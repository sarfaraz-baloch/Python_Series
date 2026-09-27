# # # Assigment Balach bali

# # class Basket:
# #     def __init__(self, location, orange):
# #         self.location = location
# #         self.orange = []
# #         self.orange.append(orange)

# #     def add_orange(self, orange):
# #         self.orange.append(orange)

# #     def customer_name(self, name , location):
# #         self.name = name
# #         self.location = location
# #         print(f"Customer name is {self.name} and location is {self.location}")
    
# #     def discard(self, orange):
# #         # empty the basket
# #         self.orange.remove(orange)

# # class Barrel(Basket):
# #     def __init__(self,size, apple):
# #         self.size = size
# #         self.apple = []
# #         self.apple.append(apple)

# #     # method overriding
# #     def add_apple(self, apple):
# #         self.apple.append(apple)


# # # Orange Class:
# # # o Attributes: weight (float), orchard (string), date_picked (string), and basket (default None).

# # class Orange:
# #     def __init__(self, weight, orchard, date_picked):
# #         self.weight = weight
# #         self.orchard = orchard
# #         self.date_picked = date_picked
# #         self.basket = None

# #     # pick(basket): Assigns the basket attribute to this orange and calls basket.add_orange(self).
# #     def pick(self, basket):
# #         self.basket = basket
# #         basket.add_orange(self)
    
# #     # squeeze(): Returns a juice amount float (e.g., weight * 0.5) and prints how much juice was squeezed.
# #     def squeeze(self):
# #         juice_amount = self.weight * 0.5
# #         print(f"{juice_amount} liters of juice obtained from the orange.")
# #         return juice_amount
    


# # # Apple Class:
# # # o Attributes: color (string), weight (float), and barrel (default None).
# # # o Methods:

# # #  pick(barrel): Assigns the barrel attribute to this apple and calls barrel.add_apple(self).

# # class Apple:
# #     def __init__(self, color, weight):
# #         self.color = color
# #         self.weight = weight
# #         self.barrel = None

# #     def pick(self, barrel):
# #         self.barrel = barrel
# #         barrel.add_apple(self)

# # # 💻 Task 3: Main Program Execution
# # # Write a main driver block at the bottom of your file to demonstrate your classes working together:
# # # 1. Instantiate Containers:
# # # o Create 1 Basket object (e.g., location: "Section A").
# # # o Create 1 Barrel object (e.g., size: 50).
# # # 2. Instantiate Fruits:
# # # o Create 2 Orange objects with different weights and orchards.
# # # o Create 2 Apple objects with different colors and weights.
# # # 3. Perform Actions:
# # # o Call .pick(basket) on both oranges to place them into your basket instance.
# # # o Call .pick(barrel) on both apples to place them into your barrel instance.
# # # o Call .squeeze() on one of the oranges.
# # # o Call .sell("Local Market") on the basket.
# # # 4. Verify State:
# # # o Print the number of items inside the basket and barrel to verify the objects were properly added.

# # # main program execution

# # # instantiate containers
# # basket = Basket("Section A")
# # barrel = Barrel(50)

# # # instantiate fruits
# # orange1 = Orange(1.2, "Orchard A", "2024-06-01")
# # orange2 = Orange(1.5, "Orchard B", "2024-06-02")
# # apple1 = Apple("Red", 0.5)
# # apple2 = Apple("Green", 0.6)

# # # perform actions
# # orange1.pick(basket)
# # orange2.pick(basket)
# # apple1.pick(barrel)
# # apple2.pick(barrel)
# # orange1.squeeze()
# # basket.sell("Local Market")

# # # verify state
# # print(f"Number of oranges in the basket: {len(basket.orange)}")
# # print(f"Number of apples in the barrel: {len(barrel.apple)}")


# # Assigment Balach bali


# class Basket:
#     def __init__(self, location):
#         self.location = location
#         self.orange = []

#     def add_orange(self, orange):
#         self.orange.append(orange)

#     def customer_name(self, name, location):
#         self.name = name
#         self.location = location
#         print(f"Customer name is {self.name} and location is {self.location}")

#     def discard(self, orange):
#         # empty the basket
#         self.orange.remove(orange)

#     def sell(self, market):
#         print(f"Basket sold to {market}")


# class Barrel(Basket):
#     def __init__(self, size):
#         self.size = size
#         self.apple = []

#     # method overriding
#     def add_apple(self, apple):
#         self.apple.append(apple)


# # Orange Class:
# # o Attributes: weight (float), orchard (string), date_picked (string), and basket (default None).

# class Orange:
#     def __init__(self, weight, orchard, date_picked):
#         self.weight = weight
#         self.orchard = orchard
#         self.date_picked = date_picked
#         self.basket = None

#     # pick(basket): Assigns the basket attribute to this orange and calls basket.add_orange(self).
#     def pick(self, basket):
#         self.basket = basket
#         basket.add_orange(self)

#     # squeeze(): Returns a juice amount float (e.g., weight * 0.5) and prints how much juice was squeezed.
#     def squeeze(self):
#         juice_amount = self.weight * 0.5
#         print(f"{juice_amount} liters of juice obtained from the orange.")
#         return juice_amount



# class Apple:
#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight
#         self.barrel = None

#     def pick(self, barrel):
#         self.barrel = barrel
#         barrel.add_apple(self)


# # main program execution

# # instantiate containers
# basket = Basket("Section A")
# barrel = Barrel(50)

# # instantiate fruits
# orange1 = Orange(1.2, "Orchard A", "2024-06-01")
# orange2 = Orange(1.5, "Orchard B", "2024-06-02")

# apple1 = Apple("Red", 0.5)
# apple2 = Apple("Green", 0.6)


# # perform actions
# orange1.pick(basket)
# orange2.pick(basket)

# apple1.pick(barrel)
# apple2.pick(barrel)

# orange1.squeeze()

# basket.sell("Local Market")


# # verify state
# print(f"Number of oranges in the basket: {len(basket.orange)}")
# print(f"Number of apples in the barrel: {len(barrel.apple)}")