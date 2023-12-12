#Leigh_Maier
#Dec 7, 2023
#P5HW
#use functions, random numbers, while numbers

#import the random library
import random 

#This function displays the main menu
def show_menu():
    print ("Welcome to Math Quiz")
    print ("MAIN MENU")
    print ("-----------------------------")
    print ("1. Adding random numbers")
    print ("2. Subtracting random numbers")
    print ("3. Exit")

#This function adds two random numbers
def add():
    ran1 = random.randint (0, 10)
    ran2 = random.randint (0, 10)
    print (f"{ran1} + {ran2}")
    return (ran1 + ran2)

#This function subtract two random numbers
def subtract():
    ran1 = random.randint (0, 10)
    ran2 = random.randint (0, 10)
    print (f"{ran1} - {ran2}")
    return (ran1 - ran2)

#This function simulates the user guessing.
#While the guess is wrong, allow the user to guess again.
def guessing(guess, correct_answer):
    num_guesses = 0
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer: #If the user guess to high
            print ("Your answer is to high")
            guess = int(input("Try again?  ")) #represents guess
        else:                      #If the user guess to low
            print ("Your answer is to low")
            guess = int(input("Try again?  ")) #represents guess
    #User answer if correct, the while loop breaks        
    print ("Your answer is Correct!")
    print (f"It took you {num_guesses} incorrect tries to get it right")           
    
#Main Function
def main():
    show_menu()
    user_option = int(input("Please choose one of the menu options:  "))

    while user_option != 3:             #This ends the program
        
        if user_option == 1:
            ran_sum = add()                 #represents the correct answer addition
            my_guess = int(input("What is the answer?  ")) #represents guess
            guessing (my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options:  "))

        if user_option == 2:
            ran_sum = subtract()                 #represents the correct answer subtraction
            my_guess = int(input("What is the answer?  ")) #represents guess
            guessing (my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose one of the menu options:  "))
        
    #If user_choice ==3, the while looop breaks
    print("Thank you for playing, Goodbye!!")

#Call the main function
if __name__ == "__main__":
    main()
