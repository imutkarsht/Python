from game_data import data
import random
from os import system

# FUNCTION TO RANDOMLY SELECT AN ITEM FROM LIST OF DATA

def show_first():
    random_data=random.choice(data)
    return random_data

# FUNCTION TO SELECT A SECOND ITEM RANDOMLY FROM LIST OF DATA (IT SHOULD NOT BE SAME AS FITST DATA)

def show_second(rd):    
    while True:
        random_data2=random.choice(data)
        if random_data2==rd:
            random_data2=random.choice(data)
        else:
            return random_data2
        
# FUNCTION TO DISPLAY DATA        
        
def print_Value(rd,ch):
    print(f"{ch}: {rd['name']} a {rd['type']} from {rd['country']}")
              
 
# MAIN DRIVER FUNCTION OF THE CODE
     
def main():
    current_score=0
    first_data=show_first()
    
    while True:
        second_data=show_second(first_data)
        
        print_Value(first_data,'a')
        print_Value(second_data,'b')     
        
        while True:
            ch=input("Who has More Followers(a/b)?").lower()
            if ch.isalpha()==False or (ch!='a' and ch!='b'):
                system('cls')
                print("Please Enter a valid Input")
            else:
                if((ch=='a' and float(first_data["followers"])>float(second_data["followers"])) or (ch=='b' and float(first_data["followers"])<float(second_data["followers"]) )  ):
                    current_score+=1
                    system('cls')
                    print(f"Right Answer you have scored {current_score} point\n")
                    first_data=second_data
                    break
         
                else:
                    system('cls')
                    print(f"You lose..... you scored {current_score} points")
                    print(f"A: {first_data['name']} has {first_data['followers']}M followers")
                    print(f"B: {second_data['name']} has {second_data['followers']}M followers")
                    return  -1    
            
           
# EXECUTION STARTS FROM HERE
        
if __name__=="__main__": 
    print("\t\t\t\tWELCOME TO THE GAME OF HIGHER AND LOWER\n\n\nBASED ON GIVEN DATA OF PERSONALITY GUESS WHETHER SECOND ONE HAS HIGHER OR LOWER NUMBER OF FOLLOWERS \nGAME WILL KEEP ON GOING UNLESS YOU GIVE A WRONG ANSWER")           
    while True:
        choice = input("\nWould You Like to Play the game(y/n)\t").lower()
        if choice == "n":
            system('cls')
            print("Bye Have a nice day...")
            break
        
        elif choice=='y':
            system('cls')
            result=main()
            if result==-1:
                continue
            
        else:
            print("Please Enter A valid response...")