#Name
#Date
#Use float values to represent the cost to drive a specified distance

#Get input from user
mpg = float (input("Enter the car's miles per gallon as a decimal numger: "))
cost_gal = float (input("Enter the cost of 1 gallon of gas: "))

#Calculate cost to drive 20 miles
#formula - miles/mpg = gal * cost per gal
drive_cost_20 = (20/mpg) * cost_gal

#Calculate cost to drive 20 miles
#formula - mpg/miles = gal * cost per gal
drive_cost_75 = (75/mpg) * cost_gal

#Calculate cost to drive 20 miles
#formula - mpg/miles = gal * cost per gal
drive_cost_500 = (500/mpg) * cost_gal

#Output the costs with 2 decimal places using an f-string
print(f"cost to drive 20 miles is {drive_cost_20:.2f}")

#Output the costs with 2 decimal places using an f-string
print(f"cost to drive 75 miles is {drive_cost_75:.2f}")

#Output the costs with 2 decimal places using an f-string
print(f"cost to drive 500 miles is {drive_cost_500:.2f}")
