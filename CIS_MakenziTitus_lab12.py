#Makenzi Titus  
#2024/07/22
#Module 12 Lab
#Design a class named pet 

#Define the class
class Pet:
    # Initialiize the pet object with name, type and age.
    def __init__(self):
        self.name = ''
        self.type = ''
        self.age = 0

    #Set attributes
    def set_name(self, name):
        self.name = name
    
    def set_type(self, pet_type):
        self.type = pet_type
    
    def set_age(self, age):
        self.age = age

    #Get attributes
    def get_name(self):
        return self.name 
    
    def get_type(self):
        return self.type
    
    def get_age(self):
        return self.age
    
    #Main Function
def main():
    
    #pet object
    pet = Pet()

    #get input from user about pet details
    name = input("Enter pets name: ")
    pet.set_name(name)
    pet_type = input("Enter pet type (cat, dog, fish, bird):")

    #Validate number for age
    while True:
        try:
            age = int(input("Enter pets age: "))
            pet.set_age(age)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number. ")

    #Display pet details
    print("\nThe pets name is:", pet.get_name())
    print("The pets type is a:", pet.get_type())
    print("The pets age is:", pet.get_age())

#run main function
if __name__ == "__main__":
    main() 