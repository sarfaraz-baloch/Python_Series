# Funcation and Recursion

#funcation defination
# def sum_calculate(a, b): #parameter
#     sum = a +b
#     print(sum)
#     return sum

# sum_calculate(2, 4) #argument and Funcation call

# summing = sum_calculate(9, 4)
# # print(summing)

# def avarage(a,b,c):
#     sum_of_avarage = a + b + c
#     avg = sum_of_avarage / 3
#     print(avg)
#     return avg

# avarage(1,2,3)

# defult Funcations using of dafulat values mean that if a user not give 
# any numbers so automatially it should caluted the default values of a funcation

# def cal_multi(a=1,b=1):
#     calc = a * b
#     print(calc)

# cal_multi(2,3)


# cities = ["Turbat", "karachi", "Lohore", "Quetta", "panjgur"]
# countrys = ["Pk", "ind", "US", "UAE", "Dubai"]

# def len_list(lenth):
#     print(len(lenth))

# len_list(cities)
# len_list(countrys)

# def print_list(city):
#     for item in city:
#         print(item, end=" ")


# print_list(cities)

# num = int(input("write a number "))
# def factroial (fact):
#     for i in range(1, num):
#         fact *= i
#         print(fact)

# factroial(num)

# usdt = 3
# exchange_rate = 83
# total = usdt * exchange_rate
# print(total)

# def converter (usdt):
#  exchange_rate = 83
#  total = usdt * exchange_rate
#  print(total)

# converter(100)

# n = int(input("write number i will guess even or ODD: "))
# def know (x):
#     if(x % 2 ==0):
#         print(f"{x} is a Even Number")
#     else:
#         print(f"{x} is a Odd Number")

# know(n)



# Recursion 
# its call a funcation itself again and again
# if we not give any condistion so Recursion Funcation run infinite and code carsh
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(10)


# def multifile(m):
#     if (m == 0):
#         return
#     multifile(m -1)
#     # multifile(3 * m)
#     print(3 * m)



# multifile(10)


# def factorial_calculate(n):
#    if (n == 0):
       
#        return 1
#    else:
#          for i in range(1, n):
#              n *= i
#          print(n)
   
# factorial_calculate(6)


# usdt = int(input("write the amount of USDT you want to convert: "))
# def converter (usdt):
#     total = usdt * 280
#     print(total)

# converter(usdt) 


# num = int(input("write a number i will guess even or ODD: "))
# def guess (x):
#     if(x %2 == 0):
#         print(f"{x} is a Even Number")
#     else:        
#         print(f"{x} is a Odd Number")

# guess(num)

# def show (n):
#     if(n == 11):
#         return
#     print(n)
#     show(n + 1)

# show(1)  

# fact = 1
# def factroial(n):
#     for i in range (1, n):  
#       n *= i
#       print(n)

# factroial(5)
        
# def mult (n):
#     if n == 0 or n == 1:
#      return 1
#     else:
#       print(n) 
#       return  mult(n-1) * n
      

# print(mult(5))

def print_list (lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    print_list(lst, idx + 1)

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
idx = 0
print_list(my_list, idx)


