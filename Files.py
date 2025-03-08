# creating file
with open("new_file.txt", "w") as file:
    file.write("new file created.")
print("File created successfully!")


# 1. Write a program to read text file

with open("new_file.txt", "r") as file:
    content = file.read()
print(content)


# 2. Write a program to write text to .txt file using  InputStream

with open("new_file.txt", "w") as file:
    file.write("Hello, this is a sample text.")


# 3. Write a program to read a file stream 

with open("new_file.txt", "rb") as file: 
    content = file.read()
    print(content.decode())  


# 4. Write a program to read a file stream supports random access 

with open("new_file.txt", "rb") as file:
    file.seek(10)  
    content = file.read(20)  
    print(content.decode())


# 5. Write a program to read a file a just to a particular index using seek() 

with open("new_file.txt", "r") as file:
    file.seek(5)  
    print(file.read(10))  


# 6. Write a program to check whether a file is having read access and write access permissions 

import os

file_path = "new_file.txt"

if os.access(file_path, os.R_OK):
    print("File has read access")
else:
    print("File does NOT have read access")

if os.access(file_path, os.W_OK):
    print("File has write access")
else:
    print("File does NOT have write access")
