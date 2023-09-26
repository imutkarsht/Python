#PYTHON PROGRAM TO GUESS THE NUMBER GAME BETWEEN AN INTERVAL

from random import randint
from os import system

# FUNCTION TO SET LOWER BOUND OF NUMBERS


def set_range_low():
    while True:
        lower_bound = input("Enter The lower bound\t")
        if lower_bound.isnumeric() == False:
            system("cls")
            print("Please Enter a Numeric value..")
        else:
            return int(lower_bound)

# FUNCTION TO SET UPPER BOUND OF NUMBERS

def set_range_up(low):
    while True:
        upper_bound = input("Enter the upper_bound\t")
        # MAKING SURE USER ONLY ENTER A NUMERIC VALUE WITH 50 GAP

        if upper_bound.isnumeric() == False:
            system("cls")
            print("Please Enter a Numeric value..")
        elif int(upper_bound) < low:
            system("cls")
            print("Upper Bound Can't be  less than lower bound")
        elif int(upper_bound) - low < 50:
            system("cls")
            print("Upper Bound and lower Bound must have a gap of 50 numbers")
        else:
            return int(upper_bound)

# FUNCTION TO GET THE GUESS OF NUMBER FROM USER

def get_number(low, up):
    while True:
        num = input("Guess The Number ")
        if num.isnumeric() == False:
            system("cls")
            print("Please Enter A numeric value only")

            # MAKING SURE VALUE IS ALWAYS IN RANGE [LOW,UP]

        elif int(num) < low or int(num) > up:
            system("cls")
            print(f"Please Enter the Number in range [{low},{up}]")
        else:
            return int(num)

# FUNCTION TO SET DIFFICULTY OF GAME BASED ON USERS CHOICE

def difficulty_set(low, up):
    print(f"I'm Thinking of a number between {low} to {up}. Can You guess it?\n")
    while True:
        dif = input("Enter 'e' for easy and 'h' for hard\t").lower()
        if dif == "e":
            no_of_attempt = 10
            return no_of_attempt
        elif dif == "h":
            no_of_attempt = 5
            return no_of_attempt
        else:
            system("cls")
            print("Please Enter a Valid response....")

# DRIVER FUNCTION OF THE CODE

def main():
    print("Enter the range in which you want to guess the number\n")
    lower_bound = set_range_low()
    upper_bound = set_range_up(lower_bound)
    Comp_num = randint(lower_bound, upper_bound)
    attempt_no = 1
    no_of_attempt = difficulty_set(lower_bound, upper_bound)
    system("cls")
    while True:
        print(f"You have {no_of_attempt-attempt_no+1} attempts left to guess the number")
        num = get_number(lower_bound, upper_bound)
        system("cls")
        if num == Comp_num:
            print(f"you won! I indeed was thinking about {Comp_num}")
            break
        elif num > Comp_num:
            print("umm you are guessing a bit high....\n")
            attempt_no += 1
        else:
            print("You are guessing a bit low..")
            attempt_no += 1

        if attempt_no > no_of_attempt:
            print(f"You were unable to guess\nYou lose\nBTW I was thinking about {Comp_num}")
            break

# Execution Starts From Here

if __name__ == "__main__":
    while True:
        print("\t\t\tWELCOME TO THE GUESS THE NUMBER GAME\n\n")
        ch = input("Would You Like to Play the game(y/n)\t").lower()
        system("cls")
        if ch == "n":
          system('cls')
          print("Bye Have a nice day...")
          break
        elif ch=='y':
          main()
        else:
          print("Please Enter A valid response...")