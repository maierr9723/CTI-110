#P4WH1
#Maier_Leigh
#11/28/2023
#Add loops to P2HW2
#Use loops to get user input

from statistics import mean

#Get number of grades from user
num_grades = int(input("How many grades will you enter?"))

#Create a list to store the grades intered
grades_list = []

#Get grades from the user
for i in range (num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}:  "))
    while grade < 0 or grade > 100:
        print("You entered an invalid grade. Please enter a valid grade.")
        grade = float(input(f"Enter grade for Module {i + 1}:  "))
        
    grades_list.append(grade)
    
print(grades_list)


#call methods on the list to get sum, avg, highest and lowest
list_sum = sum(grades_list)
list_avg = mean(grades_list)
list_min = min(grades_list)
list_max = max(grades_list)

print('\n')
print("--------Results--------")

#Output to user formatted with f-string
print(f"Lowest Grade:   {list_min:.2f}")
print(f"Highest Grade:  {list_max:.2f}")
print(f"Sum of Grade:   {list_sum:.2f}")
print(f"Average:        {list_avg:.2f}")

