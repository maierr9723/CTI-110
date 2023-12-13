#Leigh Maier
#11/09/23
#manipulating strings and intergers

#Get input from user
print("This program calculates and displays travle expenses")

budget = int(input("Enter Budget:"))

destination = input("Enter your travel destination:")

gas = int(input("How much do you think you will spend on gas?"))

hotel = int(input("Approximately, how much will you need for accomodation/hotel?"))

food = int(input("Last, how much do you need for food?"))

print("----------Travel Expenses----------")

print("Location:",destination)
print("Initial Budget:",budget)

print("Fuel:",gas)
print("Accomodation:",hotel)
print("Food",food)

print("Remaining Balance:",budget-gas-hotel-food)
