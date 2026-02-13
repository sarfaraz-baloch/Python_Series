# # This is Lecature 

# # 1 String
# # String is a data type that stores a sequence of characters

# # escape sequence characters are special characters that are used to represent other characters in a 
# # 1 is /n 
# # 2 is /t
# # 3 is \'
# # 4 is \"
# # 5 is \\

# # \n is new line
# val1 = "my name is sarfaraz.\ni am a student"
# # print(val1)

# # \t is tab
# val2 = "my name is sarfaraz.\ti am a student"
# # print(val2)


# # Basic operations in Python
# # Concatenation

# val3 = "hello"
# val4 = "world"
# # print(val3 + val4)

# # length len()

# val5 = "hello"
# val6 = len(val5)
# # print(val6 + 5)

# # indexing 

# ind1 = 'Apna collage'
# ind2 = ind1[3]
# # print(ind2)

# # concatenation with indexing and string
# # print(ind2 + "pple") 

# # Slicing 
# # Postive case 
# slice1 = 'Apna collage'
# slice2 = slice1[0:5] # starting 0 mean A and ending 5 mean ending with Apna
# slice3 = slice1[5:11] # starting 5 mean C and ending 11 mean ending with collage
# # print(slice2)
# # print(slice3)
# # print(slice2[0] + slice3) # concetening indexing and Slice 

# # Negative case
# slice4 = 'Apple'
# slice5 = slice4[-5:-1] # starting -5 mean A and ending -1 mean ending with e
# # print(slice5 )

# # String Functions
# # endswith()  to check the string ends with a particular character or substring
# str1 = "i am a student"
# # print(str1.endswith("ent")) # True
# # print(str1.endswith("abc")) # False

# # Captialization capitalize()  to convert the first character of the string to uppercase
# str2 = "hello world"
# # print(str2.capitalize())

# # replace()  to replace a substring with another substring
# str3 = "i am a student"
# # print(str3.replace("student", "teacher"))
# # print(str3.replace("a", "o"))

# # find()  to find the index of the first occurrence of a substring
# str4 = "hello world"
# # print(str4.find("world"))
# # print(str4.find("d"))
# # print(str4.find("z")) # if not found then return -1

# # count()  to count the number of occurrences of a substring
# str5 = "i am a student and i am a good student"
# # print(str5.count("student"))
# # print(str5.count("good")) 
# # print(str5.count("teacher"))  # if not found then return 0

# # student = input("Enter your name: ")
# # length = len(student)
# # continuee = student.count("r")
# # print (length * continuee)


# # conditional statements

# # light = "green"

# # if (light == "red"):
# #     print("stop")
# # elif(light == "green"):
# #     print("go")
# # else:
# #     print("wait")

# # Marks = input("Enter your marks: ")
# # marks = int(Marks)
# # if (marks >= 90):
# #     print("A+")
# # elif(marks >= 80):
# #     print("A")
# # elif(marks >= 70):
# #     print("B+")
# # elif(marks >= 60):
# #     print("B")
# # elif(marks >= 50):
# #     print("C")
# # else:
# #     print("Fail")



# # student_name = input("Enter your name: ")
# # marks_obtained = int(input("Enter your marks: "))
# # if (marks_obtained >= 90):
# #     grade = "A+"
# # elif(marks_obtained >= 80 and marks_obtained < 90):
# #     grade = "A"
# # elif(marks_obtained >= 70 and marks_obtained < 80):
# #     grade = "B+"    
# # elif(marks_obtained >= 60 and marks_obtained < 70):
# #     grade = "B"
# # elif(marks_obtained >= 50 and marks_obtained < 60):
# #     grade = "C"
# # else:
# #     grade = "Fail"
# # print("Name:", student_name)
# # print("Marks:", marks_obtained)
# # print("Grade:", grade)


# # Nesting conditional statements
# Age= int(41)

# # if(Age >= 18):
# #     if(Age >= 40):
# #         print("cannot drive above 40")
# #     else:
# #         print("can drive")
   
# # else:
# #     print("You are not eligible to drive")


# # 1 Partice
# # write a program to check Number is even or odd

# # number = int(input("Enter a number: "))
# # if (number % 2 == 0):
# #     print("Even")
# # else:
# #     print("Odd")

# # 2 Partice
# # write a program to check a umber wiche is Greater?

# # num1 = int(input("write a number"))
# # num2 = int(input("write a number"))
# # num3 = int(input("write a number"))

# # if (num1 >= num2) and (num1 >= num3):
# #     print(num1 ,"num1 is greater")
# # elif (num2 >= num1) and (num2 >= num3):
# #     print(num2 , "num2 is greater")
# # else:
# #     print(num3 , "greater")


# # x = int(input("write a number which should be multifile of 7 : "))

# # if(x % 7 == 0):
# #     print( "Yes!" +  str(x) + "number is divided by 7 or raminder of 7")
# # else:
# #     print(  "No!" + str(x) + " number is not divided by 7 or raminder of 7")


# num1 = int(input("write a number 1 : "))
# num2 = int(input("write a number 2 : "))
# num3 = int(input("write a number 3 : "))
# num4 = int(input("write a number 4 : "))

# if(num1 >= num2 and num1 >= num3 and num1 >= num4):
#     print(num1 , "num1 is greater")
# elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
#     print(num2 , "num2 is greater")
# elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
#     print(num3 , "num3 is greater")
# else:
#     print(num4 , "num4 is greater")

# # end of lecature 2

# partice 

my_name = 'My name is Ali\n in am learning python'
# print(my_name)

single_quote = 'He said, "Hello!" '
double_quote = "He said , Hello!"
# print(single_quote)
# print(double_quote)


a = "hello"
b = "python"
# print(a + b)

str_length = 'Apna college'
# print(len(str_length))

# student_name = input("Enter your name: ")
# x=  student_name.count("a")
# print(x)


text = "Apna collage"
# print(text[3:4] + "ppl" + text[11:]) 

student_String = "i am student"
# print(student_String.endswith('ent'))

capitalized_str = "hello world"
# print(capitalized_str.capitalize())
# print(capitalized_str.find('d'))

replaced_str = "i am a student"
# print(replaced_str.replace("student", "teacher"))

count_str = "i am a student and i am a good student"
# print(count_str.count("student"))
print(text[3] + "ppl")

trafic_light = "yellow"

if(trafic_light == 'red'):
    print("stop")
elif(trafic_light == 'green'):
    print("go")
else:
    print("wait")


# user_marks = int(input("Enter your marks: "))
# if(user_marks >= 80):
#     print("A+")
# elif(user_marks >= 70):
#     print("A")
# elif(user_marks >= 60):
#     print("B+")
# elif(user_marks >= 50):
#     print("B")
# elif(user_marks >= 40):
#     print(" C")
# else:
    print("Fail")

# age = int(39)

# if(age >= 18):
#     if(age >= 40):
#         print("not allowed to drive")
#     else:
#         print("allowed to drive")
# else:
#     print("not eligible")


# number = int(input("Enter a number: "))
# if(number % 2 == 0):
#     print("Even")
# else:   
#     print("Odd")

num1 = 23
num2 = 45
num3 = 12

if(num1 >= num2 and num1 >= num3):
    print(num1 , "num1 is greater")
elif(num2 >= num1 and num2 >= num3):
    print(num2 , "num2 is greater")
else:
    print(num3 , "num3 is greater")

check_whether = int(input("Enter a number to check whether it is multiple of 7: "))
if (check_whether % 7 == 0):
    print("Yes! " + str(check_whether) + " is multiple of 7")
else:
    print("No! " + str(check_whether) + " is not multiple of 7")