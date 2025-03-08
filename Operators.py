# 1. Write a function for arithmetic operators(+,-,*,/) 

def arithmetic_operations(a, b):
    print("Addition:", a + b)      
    print("Subtraction:", a - b)    
    print("Multiplication:", a * b) 
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not possible (division by zero)")


arithmetic_operations(63, 9)

# 2. Write a method for increment and decrement operators(++, --) 

def increment_decrement():
    x = 22
    
    x += 1  
    print("After Increment:", x)

    x -= 1  
    print("After Decrement:", x)

increment_decrement()

# 3. Write a program to find the two numbers equal or not.

x = int(input())
y = int(input())

if x == y:
    print("Equal")
else:
    print("Not Equal")

# 4. Program for relational operators (<,<==, >, >==)

a = 3
b = 25
print(a<b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

# 5. Print the smaller and larger number

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

smaller = min(x, y)
larger = max(x, y)

print("Smaller number:", smaller)
print("Larger number:", larger)
