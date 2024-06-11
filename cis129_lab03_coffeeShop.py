# File: cis129_lab03_coffeeShop.py
# Author: [Makenzi Titus]
# Date: [2024-06-11]
# Description: This program simulates a Coffee Shop where users can purchase coffee and muffins.
# It calculates the total cost including tax and displays a receipt.

# Function to calculate subtotal
def calculate_subtotal(coffee_quantity, muffin_quantity):
    coffee_price = 5
    muffin_price = 4
    subtotal = (coffee_price * coffee_quantity) + (muffin_price * muffin_quantity)
    return subtotal

# Function to calculate tax
def calculate_tax(subtotal):
    tax_rate = 0.06
    tax = subtotal * tax_rate
    return tax

# Function to generate receipt
def generate_receipt(coffee_quantity, muffin_quantity, subtotal, tax):
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffee_quantity} Coffee at $5 each: ${coffee_quantity * 5:.2f}")
    print(f"{muffin_quantity} Muffins at $4 each: ${muffin_quantity * 4:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    total = subtotal + tax
    print(f"Total: ${total:.2f}")
    print("***************************************")

# Main function
def main():
    print("***************************************")
    print("Welcome to My Coffee and Muffin Shop")
    print("***************************************")
    coffee_quantity = int(input("Number of coffees bought? "))
    muffin_quantity = int(input("Number of muffins bought? "))
    subtotal = calculate_subtotal(coffee_quantity, muffin_quantity)
    tax = calculate_tax(subtotal)
    generate_receipt(coffee_quantity, muffin_quantity, subtotal, tax)
    print("Thank you for visiting! We hope to see you again soon.")

# Execute the main function
if __name__ == "__main__":
    main()


= RESTART: C:/Users/kenzi/AppData/Local/Programs/Python/Python312/coffeeshop.py
***************************************
Welcome to My Coffee and Muffin Shop
***************************************
Number of coffees bought? 1
Number of muffins bought? 2
***************************************
My Coffee and Muffin Shop Receipt
1 Coffee at $5 each: $5.00
2 Muffins at $4 each: $8.00
6% tax: $0.78
---------
Total: $13.78
***************************************
Thank you for visiting! We hope to see you again soon.
