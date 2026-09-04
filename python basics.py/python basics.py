#Python Basics: Variables, Data Types and Type Conversion
# 1. Variables
# A variable is a name used to store a value in a program.
name = "Guru"
age = 22

print("Name:", name)
print("Age:", age)
# Output:
# Name: Guru
# Age: 22
#2. Data Types

# a) int - Integer
number_of_students = 30
print("Number of students:", number_of_students)
print(type(number_of_students))
# Output:
# Number of students: 30
# <class 'int'>

# b) float - Decimal Number
# A float is used to store numbers with decimal points.
product_price = 99.50

print("Product Price:", product_price)
print(type(product_price))
# Output:
# Product Price: 99.5
# <class 'float'>

# c) str - String
# A str is used to store text or characters.
customer_name = "Guru"

print("Customer Name:", customer_name)
print(type(customer_name))
# Output:
# Customer Name: Guru
# <class 'str'>


# d) bool - Boolean
# A bool stores only two possible values: True or False
is_adult = age >= 18

print("Is the person an adult?", is_adult)
print(type(is_adult))
# Output:
# Is the person an adult? True
# <class 'bool'>

# 3. Type Conversion

# Type conversion means converting a value from one data type to another.

# Example: Converting String to Integer
print("Before conversion:", type(age))
age = int(age)
print("After conversion:", type(age))
print("Age after 5 years:", age + 5)
# Output:
# Before conversion: <class 'str'>
# After conversion: <class 'int'>
# Age after 5 years: 27

# Complete Practical Example
# Variables and Data Types
salary = 25000.50   # Float

# Type Conversion
age = int(age)

# Boolean value
is_adult = age >= 18

# Output
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Is Adult:", is_adult)

# Output:
# Name: Guru
# Age: 22
# Salary: 25000.5
# Is Adult: True
