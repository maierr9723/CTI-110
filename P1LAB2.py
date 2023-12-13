#Leigh_Maier
#P4LAB2
#11/28/2023
#Use a for loop iwth the range function

#Get input from user

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an interger larger the the first number: "))

#if the first number is smaller
if num1 < num2:
    for i in range (num1,num2 +1,5):
        print(i)

else:
        #While the input is invalid
    while num1 > num2 or num1 == num2:
        #Get input from user
        print("First number must be smaller")
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an interger larger the the first number: "))        

    for i in range (num1,num2 +1,5):
        print(i)
