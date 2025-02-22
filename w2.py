def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
numbers = [1, 2, 3, 4]
print(multiply_list(numbers))

def is_perfect_number(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
print(is_perfect_number(6))

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("I am Gay"))

def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(s.lower())
print(is_pangram("Never say you are a good friend"))

def sum_of_digits(num1):
    return sum(int(digit) for digit in str(num1))
print(sum_of_digits(12345))

import random

def generate_random_numbers():
    return [random.randint(0, 100) for _ in range(4)]
print(generate_random_numbers()) 