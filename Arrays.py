# 1. Write a function to add integer values of an array 

def sum_of_array(arr):
    return sum(arr)

numbers = list(map(int, input().split()))
print("Sum of array:", sum_of_array(numbers))

# 2. Write a function to calculate the average value of an array of integers

def average_of_array(arr):
    if len(arr) == 0:
        return 0 
    return sum(arr) / len(arr)

numbers = list(map(int, input().split()))
print("Average of array:", average_of_array(numbers))


# 3. Write a program to find the index of an array element

def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return "Element not found"

numbers = list(map(int, input().split()))
element = int(input())
print("Index of", element, ":", find_index(numbers, element))


# 4. Write a function to test if array contains a specific value

def contains_value(arr, value):
    return value in arr

numbers = list(map(int, input().split()))
value = int(input())
if contains_value(numbers, value):
    print(f"The array contains the value {value}.")
else:
    print(f"The array does not contain the value {value}.")


# 5. Write a function to remove a specific element from an array

def remove_element(arr, element):
    try:
        arr.remove(element)
        print(f"Element {element} removed successfully.")
    except ValueError:
        print(f"Element {element} not found in the array.")

numbers = list(map(int, input().split()))
element = int(input())
remove_element(numbers, element)
print("Updated array:", numbers)


# 6. Write a function to copy an array to another array

def copy_array(arr):
    return arr.copy()

original_array = list(map(int, input().split()))
copied_array = copy_array(original_array)

print("Original Array:", original_array)
print("Copied Array:", copied_array)


# 7. Write a function to insert an element at a specific position in the array

def insert_element(arr, index, element):
    if index < 0 or index > len(arr):
        print("Invalid index")
    else:
        arr.insert(index, element)
        print(f"Element {element} inserted at index {index}.")

numbers = list(map(int, input("Array:").split()))
index = int(input("index number:"))
element = int(input("new element:"))
insert_element(numbers, index, element)
print("Updated array:", numbers)

# 8. Write a function to find the minimum and maximum value of an array

def find_min_max(arr):
    if not arr:
        return "Array is empty"
    return min(arr), max(arr)

numbers = list(map(int, input().split()))
minimum, maximum = find_min_max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)


# 9. Write a function to reverse an array of integer values 

def reverse_array(arr):
    return arr[::-1] 

numbers = list(map(int, input().split()))
reversed_numbers = reverse_array(numbers)

print("Original array:", numbers)
print("Reversed array:", reversed_numbers)


# 11. Write a program to find the common values between two array

def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))  

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

common_values = find_common_values(array1, array2)
print("Common values:", common_values)


# 12. Write a method to remove duplicate elements from an array 

def remove_duplicates(arr):
    return list(set(arr))  
  
numbers = list(map(int, input().split()))
unique_numbers = remove_duplicates(numbers)

print("Array without duplicates:", unique_numbers)


# 13. Write a method to find the second largest number in an array

def second_largest(arr):
    unique_numbers = list(set(arr)) 
    if len(unique_numbers) < 2:
        return "No second largest number"
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]  

numbers = list(map(int, input().split()))
print("Second largest number:", second_largest(numbers))


# 14. Write a method to find the second largest number in an array 

def second_largest(arr):
    unique_numbers = list(set(arr)) 
    if len(unique_numbers) < 2:
        return "No second largest number"
    unique_numbers.sort(reverse=True)  
    return unique_numbers[1]  

numbers = list(map(int, input().split()))
print("Second largest number:", second_largest(numbers))


# 15. Write a method to find number of even number and odd numbers in an array

def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

numbers = list(map(int, input().split()))
even, odd = count_even_odd(numbers)

print("Even numbers count:", even)
print("Odd numbers count:", odd)


# 16. Write a function to get the difference of largest and smallest value 

def difference_max_min(arr):
    if not arr:
        return "Array is empty"
    return max(arr) - min(arr)

numbers = list(map(int, input().split()))
print("Difference between largest and smallest:", difference_max_min(numbers))


# 17. Write a method to verify if the array contains two specified elements(12,23)

def contains_elements(arr, elem1=12, elem2=23):
    return elem1 in arr and elem2 in arr

numbers = list(map(int, input().split()))
print("Contains 12 and 23:", contains_elements(numbers))


# 18. Write a program to remove the duplicate elements and return the new array

def remove_duplicates(arr):
    return list(set(arr))  

numbers = list(map(int, input().split()))
unique_numbers = remove_duplicates(numbers)

print("Array without duplicates:", unique_numbers)
