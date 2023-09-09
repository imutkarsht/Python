import random
import os
# Creating and Initialising the Board using lists
row1=["➖","➖","➖"]
row2=["➖","➖","➖"]
row3=["➖","➖","➖"]

board=[row1,row2,row3]

comp_response="❌"

#function to reset the board
def reset_board():
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]="➖"
            
# Function to Print Entire Board
def print_board():
    print(*row1,sep=" ")
    print(*row2,sep=" ")
    print(*row3,sep=" ")
    
# Function to take Input of Row and column from User and return the value

def user_input_row():
    a=int(input("Row: "))
    return a

def user_input_col():
    b=int(input("Column: "))
    return b    

# function to check  if board is full...
def isfull(board):
    if("➖" in board==False):
        return 1
    else:
        return 0
    
# Function to randomly generate value of Row and column based on user Input and avaliable space and return it
def randomise_comp_col(board):
    if ("➖" in row1 or "➖" in row2 or "➖" in row3 == True):
        comp_col=random.randint(0,2)
        return comp_col
    else:
        return -1

def randomise_comp_row(board):
    if ("➖" in row1 or "➖" in row2 or "➖" in row3 == True):
        comp_row=random.randint(0,2)
        return comp_row
    else:
        return -1
    
#Function to check for avaliable blank space on board and fill accordingly

def check_blankspace(board,a,b):
    flag=-1
    if(board[a-1][b-1]=="➖"):     
        board[a-1][b-1]="⭕"
        flag=0
        return flag
    else:
        print("sorry this place is already filled... Try again")   
        return flag 
    
# function to define all different win situation and pick winner accordingly  

def checkifwin(board):
    
    R1=[board[0][0],board[0][1],board[0][2]]
    R2=[board[1][0],board[1][1],board[1][2]]
    R3=[board[2][0],board[2][1],board[2][2]]
    C1=[board[0][0],board[1][0],board[2][0]]
    C2=[board[0][1],board[1][1],board[2][1]]
    C3=[board[0][2],board[1][2],board[2][2]]
    D1=[board[0][0],board[1][1],board[2][2]]
    D2=[board[0][2],board[1][1],board[2][0]]

    val= ["⭕","⭕","⭕"]
    val2=["❌","❌","❌"]
    if(R1==val or R2==val or R3==val or C1==val or C2==val or C3==val or D1==val or D2==val):
        return 'p'
    
    elif(R1==val2 or R2==val2 or R3==val2 or C1==val2 or C2==val2 or C3==val2 or D1==val2 or D2==val2):
        return 'c'
    elif(("➖" in row1 or "➖" in row2 or "➖" in row3 ) == False):
        return 'd'
    else:
        return -1    
                      
# Driver Function 

def driver_fun():
    player_score=0
    comp_score=0
    while(True):
        reset_board()               # reseting board at the start of the every game
        game_not_ended=True
        while game_not_ended:
            # Taking Vlaue of row and column in range [0,2]
            cor_in1=0
            while(cor_in1==0):
                user_row=user_input_row()
                if(user_row<1 or user_row>3):
                    print("Out of Range value! please enter value in range")
                else:
                    cor_in1=1
                  
                    
            cor_in2=0     
            while(cor_in2==0):
                user_col=user_input_col()
                if(user_col<1 or user_col>3):
                    print("Out of Range value! please enter value in range")
                else:
                    cor_in2=1  
                    
            os.system('clear')
            comp_col=randomise_comp_col(board)
            comp_row=randomise_comp_row(board)       
            
            # Filling Board only on spaces balnk....
            
            f= check_blankspace(board,user_row,user_col)
                    
            if(f!=-1):  
                comp_flag=0
                while(comp_flag!=1):
                    if(comp_row==-1 and comp_col==-1):
                        break      
                    elif(board[comp_row][comp_col]!="➖"):
                        comp_col=randomise_comp_col(board)
                        comp_row=randomise_comp_row(board)
                    else:
                        board[comp_row][comp_col]="❌"
                        comp_flag=1 
                            
            # Checking Whether a result occured in the game
                    
                gameflag=checkifwin(board)
                if(gameflag=='p'):
                    print("Player Won!")
                    player_score=player_score+1
                    game_not_ended=False
                    
                elif(gameflag=='c'):
                    print("Computer won!") 
                    comp_score=comp_score+1
                    game_not_ended=False
                    
                elif(gameflag=='d'):
                    print("It was a Draw")                  
                    game_not_ended=False
                    
                print_board()   
                
        ch=input("Want to play again(y/n)?") 
        if(ch!='y'):
            print(f"Final Scores are....PLAYER: {player_score}\tCOMPUTER: {comp_score}")
            break   

if __name__=="__main__":
    print("Hello Welcome to the game of TIC TAC TOE... You will go first\nYou are ⭕ and Computer is ❌\nhere you go...\nEnter The value of Row and column Where you want to Enter your response\nValue of Row and column entered must be in range [1,3]")            
    driver_fun()                      