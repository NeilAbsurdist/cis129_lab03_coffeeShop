"""
Author: Neil Pritchett
Course: CIS129 Programming and Problem Solving I
Assignment: Module 3 Lab - Coffee Shop Simulator
Date: 2/18/25

Description:
This program calculates the cost of coffee, muffins, tea, and cookies,
including a 6% tax. The user inputs the quantity for each item, and
the program calculates the subtotal, tax, and total. It then prints a 
formatted receipt and thanks the customer for their purchase.
"""

# Prices of items
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
TEA_PRICE = 3.00
COOKIE_PRICE = 2.50
TAX_RATE = 0.06  # 6% sales tax

# Get user input for each item
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_teas = int(input("Number of teas bought? "))
num_cookies = int(input("Number of cookies bought? "))

# Calculate costs
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE) + \
           (num_teas * TEA_PRICE) + (num_cookies * COOKIE_PRICE)
tax = subtotal * TAX_RATE
total = subtotal + tax

# Display receipt
print("\n***************************************")
print("        My Coffee and Snack Shop       ")
print("***************************************")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE:.2f} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE:.2f} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{num_teas} Tea at ${TEA_PRICE:.2f} each: ${num_teas * TEA_PRICE:.2f}")
print(f"{num_cookies} Cookie at ${COOKIE_PRICE:.2f} each: ${num_cookies * COOKIE_PRICE:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")

# Add a thank-you message at the end
print("\nThank you for visiting My Coffee and Snack Shop! ☕🍪")
print("We appreciate your business and hope to see you again soon! 😊")
