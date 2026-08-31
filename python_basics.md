Absolutely. Let's learn these Python basics **step by step**, using one practical example throughout.

# 1. What is Python?

**Python** is a high-level, interpreted programming language used to develop:

* Web applications
* Automation scripts
* Data analysis
* Artificial Intelligence / Machine Learning
* APIs and backend systems
* Testing
* Desktop applications

### Why is Python popular?

Python has simple and readable syntax.

For example, to print something:

```python
print("Hello World")
```

Compared with many other programming languages, Python requires less code to perform the same task.

---

# 2. Installing Python

You can download Python from the official Python website:

[Python Official Website](https://www.python.org/)

After installation, open **Command Prompt** and check:

```bash
python --version
```

You may see something like:

```text
Python 3.13.5
```

You can also use **VS Code** to write Python programs.

---

# 3. Running a Python Program

Create a file:

```text
student.py
```

Write:

```python
print("Hello, Python")
```

Run it from Command Prompt:

```bash
python student.py
```

Output:

```text
Hello, Python
```

---

# 4. Variables in Python

A **variable** is a name used to store a value.

Example:

```python
name = "Rahul"
age = 25
salary = 35000.50
is_working = True
```

Here:

| Variable     | Value      | Data Type |
| ------------ | ---------- | --------- |
| `name`       | `"Rahul"`  | String    |
| `age`        | `25`       | Integer   |
| `salary`     | `35000.50` | Float     |
| `is_working` | `True`     | Boolean   |

Python automatically determines the data type based on the value.

---

# 5. Python Data Types

The four basic data types you mentioned are:

### 1. `int` — Integer

Used for **whole numbers**.

```python
age = 25
quantity = 10
```

Examples:

```text
10
25
100
-5
```

You can check the type using:

```python
age = 25

print(type(age))
```

Output:

```text
<class 'int'>
```

---

### 2. `float` — Decimal numbers

Used for numbers containing decimal values.

```python
salary = 35000.50
price = 499.99
```

Example:

```python
price = 499.99

print(type(price))
```

Output:

```text
<class 'float'>
```

---

### 3. `str` — String

Used to store **text**.

Strings are written inside quotes.

```python
name = "Rahul"
city = "Hyderabad"
material = "Samsung S24"
```

Example:

```python
name = "Rahul"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

### 4. `bool` — Boolean

Boolean has only two possible values:

```python
True
False
```

Example:

```python
is_employee = True
is_manager = False
```

For example:

```python
is_employee = True

print(type(is_employee))
```

Output:

```text
<class 'bool'>
```

---

# 6. Practical Example — Employee Information

Let's combine all four data types.

Imagine you're creating a small **employee management program**.

```python
employee_name = "Rahul"
employee_age = 25
employee_salary = 35000.50
is_employee = True

print(employee_name)
print(employee_age)
print(employee_salary)
print(is_employee)
```

Output:

```text
Rahul
25
35000.5
True
```

So:

```text
employee_name  → "Rahul"     → str
employee_age   → 25          → int
employee_salary → 35000.50   → float
is_employee    → True        → bool
```

---

# 7. How to Check Variable Type

Python provides the `type()` function.

```python
employee_name = "Rahul"
employee_age = 25
employee_salary = 35000.50
is_employee = True

print(type(employee_name))
print(type(employee_age))
print(type(employee_salary))
print(type(is_employee))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

This is very important when learning Python.

---

# 8. Type Conversion

**Type conversion** means changing one data type into another.

Python provides functions such as:

```python
int()
float()
str()
bool()
```

### String → Integer

```python
age = "25"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

---

### Integer → Float

```python
age = 25

age = float(age)

print(age)
```

Output:

```text
25.0
```

---

### Integer → String

```python
age = 25

age = str(age)

print(age)
print(type(age))
```

Output:

```text
25
<class 'str'>
```

---

# 9. Input and Output

There are two very important functions:

### `print()`

Used to **display/output** information.

```python
print("Hello")
```

Output:

```text
Hello
```

### `input()`

Used to **take input from the user**.

```python
name = input("Enter your name: ")

print(name)
```

If the user enters:

```text
Rahul
```

Output:

```text
Rahul
```

---

# 10. Important Point About `input()`

This is very important for interviews.

**`input()` always returns a string.**

For example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
25
```

Python considers it:

```text
"25"
```

not:

```text
25
```

Therefore:

```python
age = input("Enter your age: ")
```

gives:

```text
str
```

If you want an integer:

```python
age = int(input("Enter your age: "))
```

Now:

```text
age → int
```

---

# 11. Practical Example — Employee Salary

Let's create a small program.

```python
name = input("Enter employee name: ")
age = int(input("Enter employee age: "))
salary = float(input("Enter employee salary: "))

print("Employee Name:", name)
print("Employee Age:", age)
print("Employee Salary:", salary)
```

Suppose the user enters:

```text
Enter employee name: Rahul
Enter employee age: 25
Enter employee salary: 35000.50
```

Output:

```text
Employee Name: Rahul
Employee Age: 25
Employee Salary: 35000.5
```

Here:

```text
name   → str
age    → int
salary → float
```

---

# 12. Practical Example Related to SAP PP

Since you're learning **SAP PP**, let's use a production example.

Suppose you want to store information about a production order:

```python
material = "Samsung S24"
order_quantity = 100
unit_price = 45000.50
order_released = True

print("Material:", material)
print("Order Quantity:", order_quantity)
print("Unit Price:", unit_price)
print("Order Released:", order_released)
```

Output:

```text
Material: Samsung S24
Order Quantity: 100
Unit Price: 45000.5
Order Released: True
```

Types:

| Variable         | Example         | Type    |
| ---------------- | --------------- | ------- |
| `material`       | `"Samsung S24"` | `str`   |
| `order_quantity` | `100`           | `int`   |
| `unit_price`     | `45000.50`      | `float` |
| `order_released` | `True`          | `bool`  |

You can think of it like this:

```text
Material       → Text       → str
Quantity       → Whole No.  → int
Price          → Decimal    → float
Released?      → Yes/No     → bool
```

---

# 13. One Complete Beginner Program

This combines **variables + data types + input + type conversion + output**:

```python
material = input("Enter material name: ")
quantity = int(input("Enter order quantity: "))
price = float(input("Enter material price: "))
released = True

total_value = quantity * price

print("\n--- Production Order Details ---")
print("Material:", material)
print("Quantity:", quantity)
print("Price:", price)
print("Order Released:", released)
print("Total Value:", total_value)
```

If the user enters:

```text
Enter material name: Samsung S24
Enter order quantity: 100
Enter material price: 45000
```

Output:

```text
--- Production Order Details ---
Material: Samsung S24
Quantity: 100
Price: 45000.0
Order Released: True
Total Value: 4500000.0
```

### What you learned here

```text
input()       → takes user input
int()         → converts to integer
float()       → converts to decimal
str           → stores text
int           → stores whole numbers
float         → stores decimal numbers
bool          → stores True/False
print()       → displays output
```

### ⭐ Remember these 5 points for an interview

1. **Python is a high-level, interpreted programming language.**
2. **A variable stores a value and Python dynamically determines its type.**
3. **`int`, `float`, `str`, and `bool` are basic Python data types.**
4. **`input()` always returns a string, so we use `int()` or `float()` when numeric input is required.**
5. **`print()` is used to display output.**
