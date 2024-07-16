#Makenzi Titus
#Module 11 Lab
#Exercise 9.2

#Function to read grades from grade.txt
def read_grades():
    try:
        with open('grades.txt', 'r') as file:
            grades = file.readlines()

        #Convert from string to float
        grades = [float(grade.strip()) for grade in grades] 

        #Show individual grade
        print("individual grades")
        for grade in grades:
            print(grade)
        
        #calculate total, count, average
        total = sum(grades)
        count = len(grades)
        average = total / count if count != 0 else 0

        #Show total, count, average
        print("Total:", total)
        print("Count:", count)
        print("Average:", average)
    
    except FileNotFoundError:
        print("The file 'grades.txt' was not found.")
    except ValueError:
        print("There was error converting grades to float")

#call function to read and display grades
read_grades()         