#Makenzi Titus
#2024/06/19
#Repetition Structures
#Calculates total number of bottles returned and payout for each week of data

totalBottles = 0
totalPayout = 0
keepGoing = "y"
while keepGoing.lower() == "y":
    totalBottles = 0  
    totalPayout = 0   
    NBR_OF_DAYS = 7
    for day in range(1, NBR_OF_DAYS + 1):
        print(f"Enter number of bottles returned for day #{day}:")
        todayBottles = int(input())
        totalBottles += todayBottles
    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    
    print(f"Total number of bottles returned: {totalBottles}")
    print(f"Total payout: ${totalPayout:.2f}")
    
    print("Do you want to enter another week’s worth of data?")
    print("(Enter y for yes, n for no)")
    keepGoing = input().lower()

print("Program ended.")