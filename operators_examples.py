# Python Operators
#Arithmetic Operators
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
 
#output
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Modulus: 0

#Comparison Operators
a = 15
b = 20

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a < b)   # Less than
print(a > b)   # Greater than
print(a <= b)  # Less than or equal to
print(a >= b)  # Greater than or equal to

#output 
False
True
True
False
True
False

#Assignment Operators
number = 10

number += 5

print(number)
#output
15

#Logical Operators
#Logical operators are and, or, and not.
age = 25
has_id = True

print(age >= 18 and has_id)

#output
True

#Membership Operators (in, not in)
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" not in fruits)

#output
True
True

#Identity Operators (is, is not)
a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)

#output 
True
False
