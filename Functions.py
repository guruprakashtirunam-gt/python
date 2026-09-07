#  Functions
#A function is a reusable block of code.

# Practical example: Calculate the total price of a product
def calculate_total():
    price = 500
    quantity = 3
    total = price * quantity

    print("Total price:", total)

calculate_total()
#Output:
#Total price: 1500

#2. Arguments & Parameters

#Parameters are variables defined inside the function.
#Arguments are the actual values passed when calling the function.

# Practical example: Calculate an employee's salary

def calculate_salary(name, basic_salary):
    print("Employee:", name)
    print("Salary:", basic_salary)

calculate_salary("Guru", 50000)
#Here:

# `name` and `basic_salary` → **Parameters**
# "Guru"` and `50000` → **Arguments**

# 3. Return Values
#The `return` keyword sends a result back from a function.

# Practical example: Calculate total bill

def calculate_bill(price, quantity):
    total = price * quantity
    return total

result = calculate_bill(500, 3)
print("Total Bill:", result)
#Output:
#Total Bill: 1500

# Why use `return`?
#You can reuse the result:

total_amount = calculate_bill(500, 3)

if total_amount > 1000:
    print("High-value order")

# 4. Lambda Functions

#A lambda function is a small, anonymous function, usually used for simple operations.
# Normal function
def add(a, b):
    return a + b

# Same function using lambda
add = lambda a, b: a + b
result = add(10, 20)
print(result)
#Output:
30
# Practical example: Apply a discount
calculate_discount = lambda price: price * 0.90
final_price = calculate_discount(1000)
print("Final Price:", final_price)
#Output:
#Final Price: 900.0
# 5. Scope: Local & Global Variables
# Local Variable
#A local variable can only be accessed inside the function where it is created.
def calculate_price():
    price = 500  # Local variable
    print(price)
calculate_price()

#This will cause an error:
#print(price)
#Because `price` exists only inside `calculate_price()`.

#Global Variable
#A global variable is created outside the function.
company = "Samsung"
def display_company():
    print(company)
display_company()
print(company)
#Output:
#Samsung
#Samsung

# 6. Recursion Basics
#Recursion means a function calls itself.
# Practical example: Countdown
def countdown(number):

    if number == 0:
        print("Start!")
        return

    print(number)

    countdown(number - 1)
countdown(5)
#Output:
5
4
3
2
1
#Start!

# How recursion works
#countdown(5)
    
#countdown(4)
    
#countdown(3)
    
#countdown(2)
    
#countdown(1)
    
#countdown(0)
    
#Stop

# Practical example: Calculate factorial
#5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number - 1)
result = factorial(5)

print("Factorial:", result)
#Output:
Factorial: 120