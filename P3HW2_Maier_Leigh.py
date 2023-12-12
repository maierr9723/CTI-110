#Leigh Maier
#11/21/23
#Use if/else to determine and employees pay

#Get user input
emp_name = input("Enter employee name: ")
emp_hours = int(input("Enter employee's hours: "))
emp_pay = float(input("Enter the emplyess's pay rate: "))

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hours = 40

#This represents if emp_hours is 40 or less
else:
    ot_hours = 0
    reg_hours = emp_hours

#Calculate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = reg_hours * emp_pay
gross_pay = reg_pay + ot_pay

#Display results

print("----------------------------")
      
print("Employee name", emp_name)

print("\n")

print(f' Number of Hours Worked    Pay Rate    Overtime Hours    Regular Hours    Gross Pay')     

print("------------------------------------------------------------------------------------")

print(f'      {emp_hours}                     {emp_pay}          {ot_hours}               {reg_hours}            {gross_pay}')   


