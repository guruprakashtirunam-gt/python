# Python Control Flow – Practical Examples

# 1. `if`, `elif`, `else`

#Used to make decisions based on conditions.

# Example: Student Grade
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
#Output:
#Grade B

# 2.Nested Conditions

# condition inside another condition is called a **nested condition**.

### Example: Employee Eligibility

age = 25
has_experience = True

if age >= 18:
    if has_experience:
        print("Eligible for the job")
    else:
        print("Experience is required")
else:
    print("Age must be at least 18")
#Output:

#Eligible for the job

# 3. `for` Loop

#A `for` loop is used to repeat a block of code for each item in a sequence.

# Example: Display Product Names

products = ["Laptop", "Mobile", "Keyboard"]

for product in products:
    print(product)

#Output:
#Laptop
#Mobile
#Keyboard

# 4. `while` Loop

#A `while` loop repeats as long as a condition is `True`.

# Example: Counting Numbers

number = 1

while number <= 5:
    print(number)
    number += 1

#Output:
1
2
3
4
5

# 5. `break`

#The `break` statement immediately stops a loop.

# Example: Stop When Number is 5

for number in range(1, 11):
    if number == 5:
        break

    print(number)

#Output:

1
2
3
4

# 6. `continue`

#The `continue` statement skips the current iteration and moves to the next iteration.

# Example: Skip Number 3

for number in range(1, 6):
    if number == 3:
        continue

    print(number)
#Output:

1
2
4
5
# 7. `pass`

#The `pass` statement is used as a placeholder when you want to leave a block of code empty.

#Example: Empty Condition

for number in range(1, 6):
    if number == 3:
        pass
    else:
        print(number)

#Output:

1
2
4
5

# Here, when the number is `3`, the `pass` statement does nothing.


