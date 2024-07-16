#Makenzi Titus
#Module 11 Lab
#Exercise 9.3

import csv

#Function to store grades in grades.csv
def store_student_grades():
    #open csv file
    with open('grades.csv', 'w', newline='') as csvfile:
        #create csv writer object
        grade_writer = csv.writer(csvfile)

        #Header row
        grade_writer.writerow(('firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'))
        
        while True:
            firstname = input("Enter students first name (or 'done' to finish.)")
            if firstname.lower() == 'done':
                break
            lastname = input("Enter students last name: ")
            try:
                exam1 = int(input("Enter first exam grade: "))
                exam2 = int(input("Enter second exam grade: "))
                exam3 = int(input("Enter third exam grade: "))
            except ValueError:
                print("Invalid input. Please eneter a valid number grade.")
                continue

            #write student info to csv file
            grade_writer.writerow([firstname, lastname, exam1, exam2, exam3])

    print("Student grades have been saved to grade.csv")
#store grades
store_student_grades()
        
