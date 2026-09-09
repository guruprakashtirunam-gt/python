#Object-Oriented Programming.py
#OOP is important for building larger projects because it helps organize code into **classes and objects**.
#1. Classes & Objects
#A **class** is a blueprint, while an **object** is an actual instance created from that blueprint.

# Example: Material

class Material:

    def display_material(self):
        print("Material: Aluminium Body")
        print("Plant: 1000")

material1 = Material()

material1.display_material()
#Output:
#Material: Aluminium Body
#Plant: 1000

#Explanation
#Class  → Material
#Object → material1

# 2. Constructors
#A **constructor** is automatically called when you create an object.

#In Python, the constructor is:
#__init__()
#Example: Employee

class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_details(self):
        print("Name:", self.name)
        print("Department:", self.department)


employee1 = Employee("Guru", "Production")

employee1.display_details()

# Output
#Name: Guru
#Department: Production

#When you create:
#employee1 = Employee("Guru", "Production")
#the `__init__()` constructor runs automatically.

# 3. Inheritance
# **Inheritance** allows one class to inherit properties and methods from another class.

#Example: Vehicle and Car
class Vehicle:

    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")


my_car = Car()

my_car.start()
my_car.drive()

#Output
#Vehicle is starting
#Car is driving

# 4. Polymorphism
# **Polymorphism** means the same method name can perform different actions depending on the object.

# Example: Different Payment Methods
class CashPayment:

    def pay(self):
        print("Payment made using Cash")


class CardPayment:

    def pay(self):
        print("Payment made using Card")


class UPIPayment:

    def pay(self):
        print("Payment made using UPI")


payments = [
    CashPayment(),
    CardPayment(),
    UPIPayment()
]


for payment in payments:
    payment.pay()
    
# Output
#Payment made using Cash
#Payment made using Card
#Payment made using UPI

#All classes use:
#pay()
#But each object performs the method differently.

# 5. Encapsulation
#**Encapsulation** means protecting and controlling access to data inside a class.
#In Python, we commonly use `__` to indicate a private attribute.

#Example: Bank Account
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount


    def get_balance(self):
        return self.__balance


account = BankAccount("Guru", 5000)

account.deposit(2000)

print("Account Holder:", account.account_holder)
print("Balance:", account.get_balance())

#Output
#Account Holder: Guru
#Balance: 7000

#The balance is protected using:
#self.__balance
#Instead of directly changing the balance, we use methods such as `deposit()`.

# 6. Abstraction
#**Abstraction** means hiding unnecessary implementation details and showing only the important functionality.
#Python provides abstraction through the `abc` module.

#Example: Payment System
from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")

class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

payment1 = CardPayment()
payment1.pay(1000)

payment2 = UPIPayment()
payment2.pay(500)

# Output
#Paid ₹1000 using Card
#Paid ₹500 using UPI
