# 1.Write a program to print your name.
print("Aasapu Sreevani Deepthi")

# 2.Write a program for a Single line comment and multi-line comments

# I'm doing assignment

"""
My Name is Deepthi
I'm currently pursuing final
At Aditya degree college
"""


# 3.Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 

integer = 10         
boolean = True       
char = 'A'             # Python treats it as strings         
float_var = 10.5         
double = 20.123456789  # Python uses float for both float and double

print(integer, type(integer))
print(boolean, type(boolean))
print(char, type(char))
print(float_var, type(float_var))
print(double, type(double))


# 4.Define the local and Global variables with the same name and print both variables and understand the scope of the variables

var = "It's a global variable"

def my_function():
    
    var = "It's a local variable"
    print("Inside function:", var)  

my_function()

print("Outside function:", var) 
