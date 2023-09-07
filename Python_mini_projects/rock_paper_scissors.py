# python program for rock paper scissors game
import random
import os
   
# Functions of the game.....
       
def RPS_game(list1,ch):
    user_ch=list1[ch-1]
    print(f"\nYOUR CHOICE:\t\t{user_ch}\n")
    
    if(user_ch==rock):
        comp_in=random.randint(0,2)
        print(f"COMPUTER'S CHOICE:\t{list1[comp_in]}\n")
        if(list1[comp_in]==rock):
            print("YOU BOTH CHOSED ROCK SO THIS ROUND IS A DRAW.....\n")
        elif(list1[comp_in]==scissors):
            print("YOUR ROCK CRUSHED COMPUTER'S SCISSORS! YOU WON THIS ROUND....\n")
            return 'a'
        else:
            print("YOUR ROCK GOT WRAPPED UP IN COMPUTER'S PAPER! YOU LOSE THIS ROUND....\n")  
            return 'b'
                  
    if(user_ch==paper):
        comp_in=random.randint(0,2)
        print(f"COMPUTER'S CHOICE:\t{list1[comp_in]}\n")
        if(list1[comp_in]==rock):
            print("YOU WRAPPED COMPUTER'S ROCK IN YOUR MIGHTY PAPER! YOU WON THIS ROUND....\n")
            return 'a'
        elif(list1[comp_in]==scissors):
            print("YOUR PAPER WAS TORNED DOWN BY COMPUTER'S SCISSORS! YOU LOSE THIS ROUND....\n")
            return 'b'
            
        else:
            print("YOU BOTH CHOSED PAPER SO THIS ROUND IS A DRAW.....\n")   
                 
    if(user_ch==scissors):
        comp_in=random.randint(0,2)
        print(f"COMPUTER'S CHOICE:\t{list1[comp_in]}\n")
        if(list1[comp_in]==rock):
            print("SADLY COMPUTER'S ROCK WAS TOO STRONG FOR YOU! YOU LOSE THIS ROUND....\n")
            return 'b'
        elif(list1[comp_in]==scissors):
            print("YOU BOTH CHOSED SCISSORS SO THIS ROUND IS A DRAW.....\n")
        else:
            print("YOU TEARED APART COMPUTER'S PAPER WITH YOY SCISSOR! YOU WON THIS ROUND....\n") 
            return 'a'
   
# Initializing value of list members....
rock="🪨"
paper="📃"
scissors="✂️"

#initialization of points scored
comp_point=0
player_point=0

list1=[rock,paper,scissors]            # creating a list with value or rock paper and scissors
choice='y'
# Running The program till user wants....

while(choice=='y'):
    print("\t\t\t\tROCK PAPER SCISSORS GAME\n\n PLEASE ENTER\n\t\t  1. FOR ROCK\t\t2. FOR PAPER\t\t3. FOR SCISSORS ")

    ch=int(input())
    
    os.system('cls')    

    ret=RPS_game(list1,ch)
   
# Point Upgradation......
    
    if(ret=='a'):
        player_point=player_point+1
    elif(ret=='b'):
        comp_point=comp_point+1
    else:
        comp_point=comp_point+0
                
    print(f"\n\t*****CURRENT SCORES*****\n\nCOMPUTER: {comp_point}\t\t\tPLAYER: {player_point}")
    
# Taking users input on whether they want to continue or not.....    

    print("\nWANT TO TRY AGAIN???.....(y/n)")
    choice=input()
    os.system('cls')
    
# Final Message after game completion.....

    if(choice=='n'):
        if(comp_point>player_point):
            
            print(f"GAME OVER.... YOU PLAYED WELL BUT SADLY COMPUTER WAS ON OTHER LEVEL YOU LOSE: {player_point} - {comp_point}")
        elif(comp_point<player_point):
            print(f"GAME OVER.... WELL DONE YOU WON! BY : {player_point} - {comp_point}")
        else:
            print(f"GAME OVER IT WAS A DRAW......{comp_point} - {player_point}")        