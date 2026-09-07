# Python Data Structures
#1. Lists
#list is an ordered and mutable collection that can store multiple values.
#Example: Shopping List

products = ["Laptop", "Mouse", "Keyboard"]
products.append("Monitor")
print(products)

#Output:
#['Laptop', 'Mouse', 'Keyboard', 'Monitor']

# 2. Tuples
#A tuple is an ordered collection of values that cannot be modified after creation.
# Example: Employee Details
employee = ("John", 101, "Developer")

print("Name:", employee[0])
print("Employee ID:", employee[1])
print("Role:", employee[2])

#Output:
#Name: John
#Employee ID: 101
#Role: Developer

# 3. Sets
#A set stores unique values. Duplicate values are automatically removed.
# Example: Unique Student IDs

student_ids = {101, 102, 103, 101, 102}

print(student_ids)

#Output:
#{101, 102, 103}

# 4. Dictionaries
#A dictionary stores data in **key-value pairs**.
# Example: Student Information

student = {
    "name": "guru",
    "age": 22,
    "course": "Python"
}

print("Name:", student["name"])
print("Course:", student["course"])
# Output:
# Name: guru
# Course: Python

# 5. String Methods
# Python provides built-in methods to perform operations on strings.
# Example: Formatting a Name

name = "python programming"

print(name.upper())
print(name.title())
print(name.replace("programming", "developer"))

# Output:
# PYTHON PROGRAMMING
# Python Programming
# python developer

# 6. List Comprehension
# List comprehension is a short and simple way to create a list.
# Example: Creating a List of Squares

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)
#Output:
#[1, 4, 9, 16, 25]

# 7. Dictionary Comprehension
# Dictionary comprehension  is a short way to create dictionaries.
# Example: Creating a Dictionary of Numbers and Squares
numbers = [1, 2, 3, 4, 5,6]
squares = {number: number ** 2 for number in numbers}
print(squares)

#Output:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}