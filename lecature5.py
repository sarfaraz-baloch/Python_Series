# Loops 
# A loop is a programming construct that repeats a block of code as long as a specified condition is true.
# 1 while loop
# 2 for loop

# count = 1
# while count <= 100:
#     print(count)
#     count += 1

# print(count)

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# Partice quetions
# print 1 To 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# print 100 To 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


# print the table of 3


# n  = int(input('Give me a number '))
# i = 1
# while i <= 10:
#     print (n * i)
#     i += 1

# Print a list of number 
# traverse mean one by one excuted the list ....

# list_Number = [1, 4, 9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(list_Number):
#     print(list_Number[idx])
#     idx += 1

# searched_items = (1, 4, 9,16,25,36,49,64,81,100)
# x = 36
# i = 0

# while i < len(searched_items):
#     if(searched_items[i] == x):
#         print("Founded it", i) 
#         break
#     else:
#         print("Not Founded")
#     i += 1

# Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
# continue Statement
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.

# Example of break statement
# i = 1
# while i <= 10:
#     print(i)
#     if (i == 5):
#         print("Breaking the loop at i =", i)
#         break

#     i += 1

# Example of continue statement
# i = 1
# while i < 10:
#    i += 1
#    if (i % 2 != 0):
#     #   i += 1
#       continue
#    print(i)
#    i += 1

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for val in num:
#     print(val)

# num = [1,2,4,9,16,25,36,49,64,81,100]
# x = 64
# idx = 0
# for val in num:
#     idx += 1
#     if val == x:
#         print(f"{x} is Found it {idx}")
#         break
#     print(val)
# else:
#     print("Done")



# Range 
# seq = range(10)   #range((stop))
# for i in seq:
#     print(i)

# for i in range(2, 10): #range(start, stop)
#     print(i)


# for i in range(2, 10, 2): #range(start, stop, step)
#     print(i)

# for i in range(1, 100):
#     print(i)


# back = 100
# for i in range(back):
#     back = back - 1
#     print(back)

# for i in range(1 , 11):
#     print(3 * i)

# n = 5 
# sum = 0
# for i in range(1,6):
#     sum = sum +i
#     print(sum)

# print('Total ', sum)  


# a = 5
# for i in range (1,5):
#     a *= i
#     print(a)




# Partice
# for i in range(1, 100):
#     print(i)


# backward = 10

# while backward >= 1:
#     backward -= 1
#     print(backward)

# for i in range (2,20,2):
#     print(i)

# for i in range (1,20, 3-1):
#     print(i)

# table = 5

# for i in range (1, 11):
#     print(table * i)

# sum = 1
# while sum <= 50:
#     sum += 1
#     if (sum == 25):
#      print(sum)
#      break
#     else:
#      print(sum)
    
# sum = 1
# while sum <=20:
#     if(sum == 3):
#         sum += 1
#         continue
#     print(sum)
#     sum += 1

# numbers = [10, 20, 30, 40, 50]

# for num in numbers:
#     print(num)


# count = 0

# for i in numbers:
#     count += 1
#     print(count, i)


# nums = [1, 3, 5, 7, 9]


# for num in nums:
#     if num == 7:
#         print(num, "exists in the list")
#         break
#     else:
#         print(num, "does not exist in the list")

# sum = 1

# for i in range(1, 10):
#     sum +=  i
#     print(sum)


# multipile = 1

# for i in range(1, 5):
#     multipile *=  i
#     print(multipile)
    
# pattern = "*"

# for i in range(1, 6):

#     print(pattern * i)
#     # print(i)

# nums = [10, 20, 30, 40, 50]
# reversed_list = []

# for i in range(len(nums)):
#     reversed_list.append(nums[i])
#     reversed_list.reverse()
#     print(reversed_list)

# nums = [1, 4, 7, 8, 10, 13, 16]
# count = 0
# for i in range(len(nums)):
#     if(nums[i] % 2 == 0):
#         count += 1
#         print(nums[i],count)
    
# user = int(input("enter a number"))
# fact = 1
# for i in range(1,user+1):
#     fact *= i
#     print(fact)

# for i in range(1, 100):
#     if i % 5 ==0 and i % 10 == 0:
#         print("divide by 5 and 10", i)
#     elif i % 5 == 0:
#         print("divide by 5", i)

# nums = [23, 45, 12, 67, 34]
# largest = 0
# for i in range(len(nums)):
#    if nums[i] > largest:
#        largest = nums[i]
# print(largest)
        
# nums = [-5, 10, -3, 7, -1, 9]

# for i in range(len(nums)):
#     if nums[i] > 0:
#         print(nums[i])


