#1. Write a program to print  “Bright IT Career”  ten times using for loop 
for i in range(10):
    print("Bright IT Career")

#2. Write a  program to print 1 to 20 numbers using the while loop. 
i=1
while i<=20:
    print(i)
    i=i+1
    
#3. Program to equal operator and not equal operators 

a,b=10,20
print("a==b",a==b)
print("a!=b",a!=b)

#4. Write a program to print the odd and even numbers. 
print("Even numbers")
for i in range(0,20,2):
    print(i)
print("odd numbers")
for i in range(1,20,2):
    print(i)
    
#5. Write a program to print largest number among three numbers. 
a, b, c = map(int, input("Enter three numbers separated by space: ").split())

if a > b and a > c:
    print("Largest number:", a)
elif b > c:
    print("Largest number:", b)
else:
    print("Largest number:", c)

#6. Write a  program to print even number between 10 and 20 using while 
i = 11
while i < 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

#7. Write a program to print 1 to 10 using the do-while loop statement. 
j = 1
while True:
    print(j, end=" ")
    j += 1
    if j > 10:
        break

#8. Write a program to find Armstrong number or not 
num = int(input("Enter a number: "))
n = num
sum_of_cubes = 0

while num > 0:
    digit = num % 10  
    sum_of_cubes += digit ** 3  
    num //= 10 

if sum_of_cubes == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
    
    
#9. Write a program to find the prime or not. 
n=int(input())

if n<2:
    print(f"{n} is not a prime number")
else:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
if prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not  a prime number")

#10. Write a program to palindrome or not. 
n=input()
if n==n[::-1]:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is a palindrome")
    
#11. Program to check whether a number is EVEN or ODD using switch 
num=int(input("enter:"))

match num%2:
    case 0:
        print(f"{n} is a even ")
    case 1:
        print(f"{n} is a odd ")
        
#12. Print gender (Male/Female) program according to given M/F using switch
gender = input("Enter gender (M/F): ").strip().upper()

match gender:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print("Invalid input")
