#Print Hello World
print("Hello, World!")

#Calculate the sum of 2 numbers
def sum(a, b):
    return a + b
result1 = sum(5, 3)
print(result1)

#Find the square of a number
def square(n):
    return n ** 2
result2 = square(4)
print(result2)

#check whether the number is even or odd
def eo(n):
    return "Even" if n % 2 == 0 else "Odd"
result = eo(7)
print(result)

#takes a list and returns a new list with unique elements of the first list
def ele(input_list):
    return list(set(input_list))
result3 = ele([1, 2, 2, 3, 4, 4, 5])
print(result3)

#convert celsius to farenheit
def ctf(celsius):
    return (celsius * 9/5) + 32
result4 = ctf(25)
print(result4)

#calculate the area of the circle
import math
def area_of_circle(radius):
    return math.pi * (radius ** 2)
result5 = area_of_circle(5)
print(result5)

#reverse a given string
def reverse_string(s):
    return s[::-1]
result6 = reverse_string("Hello")
print(result6)

#If a number is prime no
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
result7 = is_prime(11)
print(result7)

#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result8 = factorial(5)
print(result8)

#largest item from a given list
def largest_item(input_list):
    return max(input_list)
result9 = largest_item([1, 2, 3, 4, 5])
print(result9)

#check a no is in a given range
def is_in_range(n, start, end):
    return start <= n <= end
result10 = is_in_range(5, 1, 10)
print(result10)

#calculate upper case letters and lower case letters in a string
def count_case(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return upper_count, lower_count
result = count_case("Hello World!")
print(result)

#accept the user's name and greet them with it
name = input("Enter your name: ")
print(f"Hello, {name}!")

