#Maier_Leigh
#11/30/2023
#P4HW2
#Create variables to hold totals paid to employees

num_emp = 0
total_reg = 0
total_ot = 0
total_gross = 0

#Get user input
emp_name = input("Enter employee name or type Done to finish: ")
#Loop to control adding employees
while emp_name != "Done":
    num_emp += 1
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
    reg_pay = reg_hours * emp_pay
    total_reg += reg_pay

    ot_pay = (emp_pay * 1.5) * ot_hours
    total_ot += ot_pay


    gross_pay = reg_pay + ot_pay
    total_gross += gross_pay

    #Display results

    print("----------------------------")
          
    print("Employee name", emp_name)

    print()

    print(f' Number of Hours Worked    Pay Rate    Overtime Hours    Regular Hours    Gross Pay')     

    print("------------------------------------------------------------------------------------")

    print(f'      {emp_hours}                     {emp_pay}          {ot_hours}               {reg_hours}            {gross_pay}')   
    print()
#Next command is asking for a new name
    emp_name = input("Enter employee name or type Done to finish: ")


#This code excutes after the code completes
print("Done adding employees")
print()
print (f"Total number of employees: {num_emp}")
print (f"Total regualar pay: {total_reg}")
print (f"Total overtime pay: {total_ot}")
print (f"Total gross pay: {total_gross}")


