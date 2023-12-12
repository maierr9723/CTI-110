#Leigh_Maier
#Dec 5, 2023
#User-defined functions lab

#This function take a bool parameter an returns an interger
def day_in_feb(is_leap):
    if is_leap == True:
        days= 29
    else:             #Represents uneven = False
        days = 28
    return days

#Create main function

def main():
    is_leap_year = False

    input_year = int(input("Enter a year:  "))

       

    if (input_year % 4) == 0:      # inputYear is divisible by 4

      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

        if (input_year % 400) == 0: # inputYear is divisible by 400

          is_leap_year = True

        else:           # inputYear is not divisible by 400

          is_leap_year = False

      else:             # inputYear is not divisible by 100

        is_leap_year = True

    else:               # inputYear is not divisible by 4

      is_leap_year = False

    if is_leap_year== True :

        print(f'{input_year } - leap year')

    else:

        print(f'{ input_year } - not a leap year')
              

    #Call our function
    num_days = day_in_feb(is_leap_year)
    print(f"The year {input_year} has {num_days} days in February")
        
    
#Call the main function:
if __name__ == "__main__":
    main()
    
