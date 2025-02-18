"""
Author: Neil Pritchett
Course: CIS129 Programming and Problem Solving I
Assignment: Module 3 Lab - Coffee Shop Simulator
Date: 2/18/25

Description:
This program calculates the cost of coffee and muffins, including a 6% tax.
The user inputs the quantity for each item, and the program calculates 
the subtotal, tax, and total. It then prints a formatted receipt.
"""

# Prices
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
TAX_RATE = 0.06  # 6% sales tax

# User input
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))

# Calculations
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE)
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display receipt
print("\n***************************************")
print("        My Coffee and Muffin Shop      ")
print("***************************************")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE:.2f} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE:.2f} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
