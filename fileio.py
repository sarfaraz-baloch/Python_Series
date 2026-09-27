# File i/o 
# python can be used to perform file i/o operations.(read and write files)
#  Types of files:
# 1. text files: .txt, .csv, .json, .xml etc.
# 2. binary files: .jpg, .png, .pdf, .docx, .xlsx, .mp3, .mp4 etc.

# File i/o operations:
# 1. open(): open a file
# 2. read(): read the contents of a file
# 3. write(): write to a file
# 4. close(): close a file


# "r " - read mode (default)

# f = open("demo.txt", "r") # open the file in read mode
# data = f.read("") # read the contents of all the file
# print(data) # print the contents of the file

# text = f.read(5) # read the first 5 characters of the file
# print(text) # print the first 5 characters of the file

# line1 = f.readline() # read the first line of the file
# print(line1) # print the first line of the file

# line2 = f.readline() # read the second line of the file
# print(line2) # print the second line of the file

# f.close() # close the file

# 2. "w" - write mode (overwrites the file if it already exists)
# f = open("demo.txt", "w") # open the file in write mode
# f.write("i want to learn python and javascript ") # write to the file
# f.close() # close the file

# 3. "a" - append mode (appends to the file if it already exists)
# f = open("demo.txt", "a") # open the file in append mode
# f.write("and i want to learn data science and machine learning") # append to the file
# f.close() # close the file

# # 4. r+ - read and write mode (allows both reading and writing to the file)
# f =open("demo.txt", "r+") # open the file in read and write mode
# f.write("abc") # write to the file (this will overwrite the first 3 characters of the file)
# print(f.read()) # read the contents of the file (this will read the contents of the file starting from the 4th character)
# f.close() # close the file  

# 5. "w+" it trancates the file to zero length if it already exists, otherwise creates a new file for reading and writing.
# f = open("demo.txt", "w+") # open the file in write and read mode
# data =f.read() 
# print(data)
# f.write("i want to learn python and javascript")
# f.close()

# 6. "a+" it opens the file for reading and appending. The file pointer is at the end of the file if the file exists.
#  That is, the file is in the append mode.
# If the file does not exist, it creates a new file for reading and writing.

# f =open("demo.txt", "a+") # open the file in append and read mode
# f.write("and i want to learn data science and machine learning") # append to the file

# f.close()