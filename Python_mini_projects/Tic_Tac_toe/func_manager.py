#Creating and Initialising the Board using lists
import random
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
                  