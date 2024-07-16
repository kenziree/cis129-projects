#Makenzi Titus
#Module 11 Lab
#figure 9.1

#function to store grades in grades.txt
def store_grades():
    with open('grades.txt', 'w') as file:
        while True:
            grade = input("Enter a grade (or -1 to finish): ")
            if grade == '-1':
                break
            try:
                float(grade) #checks if input is valid number
                file.write(grade = '\n')
            except ValueError:
                print("Invalid input. Please enter a valid number grade.")
    print("Grades have been saved to grades.txt")

#Store grades
store_grades()

#verify grades.txt
print("\n Grades stored in file:")
with open('grades.txt', 'r') as file: 
    grades = file.readlines()
    for grade in grades:
        print(grade.strip())
