# Coffee Shop Simulator
# Author: Makenzi Titus
# Date: 2024-06-11
# This program simulates a coffee shop order system and calculates a receipt based on user input.

def main():
    # Prices
    coffee_price = 5
    muffin_price = 4
    tax_rate = 0.06

    # Get the number of coffees and muffins from the user
    print("***************************************")
    print("My Coffee and Muffin Shop")
    coffees = int(input("Number of coffees bought?1 "))
    muffins = int(input("Number of muffins bought?2 "))
    print("***************************************\n")

    # Calculate costs
    coffee_cost = coffees * coffee_price
    muffin_cost = muffins * muffin_price
    subtotal = coffee_cost + muffin_cost
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Display the receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffees} Coffee at $5 each: ${coffee_cost:.2f}")
    print(f"{muffins} Muffins at $4 each: ${muffin_cost:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")

if __name__ == "__main__":
    main()
