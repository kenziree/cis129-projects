# Module 4 Lab-4
# Makenzi Titus
# 06/12/2024
# If statements
# Determine Bonuses
# Predefined monthly sales and sales increase values from chart or data
monthlySalesValues = [120500, 93400, 75000, 82000, 125000]
salesIncreaseValues = [5, 5, 1.5, 3.6, 4.5]

# Function to calculate bonuses based on input values
def calculate_bonuses(monthlySales, salesIncrease):
    # Declare local variables
    storeAmount = 0   # store bonus amount
    empAmount = 0     # employee bonus amount

    # This code determines the store bonus
    if monthlySales >= 110000:
        storeAmount = 6000
    elif 95000 <= monthlySales < 110000:
        storeAmount = 4000
    elif 75000 <= monthlySales < 95000:
        storeAmount = 3000
    elif 50000 <= monthlySales < 75000:
        storeAmount = 2000
    else:
        storeAmount = 0

    # This code determines the employee bonus
    if salesIncrease >= 5:
        empAmount = 75
    elif salesIncrease >= 4:
        empAmount = 50
    elif salesIncrease >= 2:
        empAmount = 40
    else:
        empAmount = 0

    # Print bonus information
    print("For monthly sales of ${:.2f} and a {:.2f}% sales increase:".format(monthlySales, salesIncrease))
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print('Congrats! You have reached the highest bonus amounts possible!')

# Loop through predefined values and calculate bonuses
for i in range(len(monthlySalesValues)):
    monthlySales = monthlySalesValues[i]
    salesIncrease = salesIncreaseValues[i]
    calculate_bonuses(monthlySales, salesIncrease)
    print()  # Add a blank line for better readability between outputs
    