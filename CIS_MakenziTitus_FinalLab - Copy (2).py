#Makenzi Titus
#Final Project
#Pseudocode
#Homelessness and a Software Solution

#Main function to start program
def main():
    display_menu()

    #Prompt user until they exit app
    while True:
        option = get_user_choice() #This will be main menu options

        if option == 1:
            show_shelters() #display nearby shelters
        elif option == 2:
            show_job_training() #lists job training programs in area
        elif option == 3:
            show_healthcare() #show a list of available healthcare services in the area
        elif option == 4:
            show_sobriety_homes() #list of sobriety homes nearby
        elif option == 5:
            show_community_support() #display community support programs for food, items, etc
        elif option == 6:
            exit_program() #exits the app/program
        else:
            print("Invalid choice. Please choose a number from the menu.")

#Function to display main menu options
def display_menu():
    print("=== Homeless Assistance Platform ===")
    print("1. Find Shelters")
    print("2. Job Training Programs")
    print("3. Healthcare Services")
    print("4. Sobriety Homes")
    print("5. Community Support")
    print("6. EXIT")

#Function for menu choice from user
def get_user_choice():
    while True:
        try:
            option = int(input("Enter your choice: "))
            return option 
        except ValueError:
            print("Invalid input. Please enter a number.")
  
#Function to show nearby shelers
def show_shelters():
    print("=== Nearby Shelters ===")
    #Will display nearby shelter info

#function to list job training programs
def show_job_training():
    print("=== Job Training Programs ===")
    #retrieves and displays job program info

#Function for Healthcare Services
def show_healthcare():
    print("=== Healthcare Services ===")
    #will display local healthcare services info

#Function for a list of sobriety homes
def show_sobriety_homes():
    print("=== Sobriety Homes ===")
    #will display local sobriety homes nearby and its info

#Function for community support options
def show_community_support():
    print("=== Community Support Options ===")
    #Shows local community support info 

#Function to exit program
def exit_program():
    print("Exiting the program. Have A Nice Day!")
    #Will close out the program and information.

#Call main funtion to start the program
main()

