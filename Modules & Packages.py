#Modules & Packages.py
#such as `math`, `random`, and `datetime`.
#1. Importing Built-in Modules
#Example: `math` module
#Suppose you want to calculate the area of a circular manufacturing component.

import math
radius = 10
area = math.pi * radius ** 2

print("Area of circle:", area)
#Output:
#Area of circle: 314.1592653589793

#2. Using the `random` Module
#Practical Example: Generate a Random Employee ID
import random
employee_id = random.randint(1000, 9999)
print("Generated Employee ID:", employee_id)
#Every time you run the program, you may get a different ID:

#Output:
#Generated Employee ID: 5824

#3. Using the `datetime` Module
#Example: Display Today's Date and Time

from datetime import datetime
current_date_time = datetime.now()
print("Current Date and Time:", current_date_time)

#You can also display it in a readable format:

from datetime import datetime

current_date = datetime.now()

print("Date:", current_date.strftime("%d-%m-%Y"))
print("Time:", current_date.strftime("%H:%M:%S"))

#4. One Complete Practical Example

import math
import random
from datetime import datetime

#Generate a production order number
production_order = random.randint(100000, 999999)

#Calculate required material quantity
quantity = 25
material_required = math.ceil(quantity * 1.10)

#Get the current date and time
production_date = datetime.now()
print("Production Order:", production_order)
print("Finished Goods Quantity:", quantity)
print("Material Required:", material_required)
print("Report Generated:", production_date.strftime("%d-%m-%Y %H:%M:%S"))

# Output:
#Production Order: 458921
#Finished Goods Quantity: 25
#Material Required: 28
#Report Generated: 08-09-2026 11:38:00