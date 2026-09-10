#File Handling in Python
#1.Reading a TXT File
#Suppose we have a file called employees.txt:

from dbm import error
from venv import create
#Guru - SAP PP
#Rahul - SAP MM
#Arun - SAP FI

#file = open("employees.txt", "r")
#data = file.read()
#print(data)

#file.close()

#output:
#Guru - SAP PP
#Rahul - SAP MM
#Arun - SAP FI

#2. Writing to a TXT File
#Suppose you want to create a production report.

with open("production.txt", "w") as file:

    file.write("Production Report\n")
    file.write("Material: ALUMINIUM BODY\n")
    file.write("Plant: 1000\n")
    file.write("Quantity: 100\n")

print("File created successfully")

#This creates:
#production.txt
#with:
#Production Report
#Material: ALUMINIUM BODY
#Plant: 1000
#Quantity: 100
#"w" means write mode.

#3. Working with CSV Files
#CSV means Comma-Separated Values.
#A CSV file is commonly used for tabular data such as:
#Material,Plant,Quantity
#ALUMINIUM BODY,1000,100
#DISPLAY PANEL,1000,50
#BATTERY,1000,75

#Python example
import csv

#with open("materials.csv", "r") as file:

    #reader = csv.DictReader(file)

    #for row in reader:
       # print("Material:", row["Material"])
       # print("Plant:", row["Plant"])
        #print("Quantity:", row["Quantity"])
        #print()

#output:
#Material: ALUMINIUM BODY
#Plant: 1000
#Quantity: 100

#Material: DISPLAY PANEL
#Plant: 1000
#Quantity: 50

#Material: BATTERY
#Plant: 1000
#Quantity: 75

#Writing a CSV file
import csv

materials = [
    ["Material", "Plant", "Quantity"],
    ["ALUMINIUM BODY", "1000", 100],
    ["DISPLAY PANEL", "1000", 50],
    ["BATTERY", "1000", 75]
]

with open("materials.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(materials)

print("CSV file created")

#4. Working with JSON
#JSON is commonly used to store structured data and exchange data between applications.
#Suppose we have an employee:

#employee = {
    #"name": "Guru",
    #"department": "SAP PP",
    #"experience": 1
#}
#Save it to JSON
import json

employee = {
    "name": "Guru",
    "department": "SAP PP",
    "experience": 1
}

with open("employee.json", "w") as file:

    json.dump(employee, file, indent=4)

print("JSON file created")
#The employee.json file will contain:
{
    "name": "Guru",
    "department": "SAP PP",
    "experience": 1
}
#Read JSON
import json

with open("employee.json", "r") as file:

    employee = json.load(file)

print("Name:", employee["name"])
print("Department:", employee["department"])
print("Experience:", employee["experience"])

#output:
#Name: Guru
#Department: SAP PP
#Experience: 1

#5. Exception Handling — try-except
#Exception handling prevents your program from crashing when an error occurs.
#example: Reading a file that doesn't exist
try:

    with open("employee.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:

    print("Error: employee.txt file does not exist")
#If employee.txt doesn't exist, instead of the program crashing, you get:
#Error: employee.txt file does not exist

#Another Practical Example: Invalid Number
#Suppose you're calculating material requirements.
try:

    quantity = int(input("Enter production quantity: "))

    material_required = quantity * 2

    print("Material Required:", material_required)

except ValueError:

    print("Please enter a valid number")
#If the user enters:
#Enter production quantity: abc

#Output:
#Please enter a valid number

#Complete Example
#Here's a small Production Report System using TXT + JSON + exception handling:
import json

try:

    material = input("Enter material name: ")
    plant = input("Enter plant: ")
    quantity = int(input("Enter production quantity: "))

    production_data = {
        "material": material,
        "plant": plant,
        "quantity": quantity
    }

    with open("production.json", "w") as file:
        json.dump(production_data, file, indent=4)

    print("Production data saved successfully")

except ValueError:

    print("Error: Quantity must be a number")

except Exception as e:

    print("Unexpected error:", e)
#Example input:

#Enter material name: ALUMINIUM BODY
#Enter plant: 1000
#Enter production quantity: 100

#Output:
#Production data saved successfully