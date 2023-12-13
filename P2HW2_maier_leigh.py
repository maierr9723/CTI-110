#CTI-110
#P2HW2 - list
#Leigh Maier
#Nov 14, 2023
#This program will show grades as sum, average, highest and lowest

from statistics import mean

#Get input from user
num1 = float(input("Enter grade for Module 1:  "))
num2 = float(input("Enter grade for Module 2:  "))
num3 = float(input("Enter grade for Module 3:  "))
num4 = float(input("Enter grade for Module 4:  "))
num5 = float(input("Enter grade for Module 5:  "))
num6 = float(input("Enter grade for Module 6:  "))

#Create an empty list
num_list = []

#Add values to list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)
num_list.append(num6)

#call methods on the list to get sum, avg, highest and lowest
list_sum = sum(num_list)
list_avg = mean(num_list)
list_min = min(num_list)
list_max = max(num_list)

print('\n')
print("--------Results--------")

#Output to user formatted with f-string
print(f"Lowest Grade:   {list_min:.2f}")
print(f"Highest Grade:  {list_max:.2f}")
print(f"Sum of Grade:   {list_sum:.2f}")
print(f"Average:        {list_avg:.2f}")
