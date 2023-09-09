import os
# ALL IMPORTANT FUNCTION DEFINITION AND DECLARATIONS ARE INSIDE USER DEFINED MODULE func_manager

import func_manager
# Driver Function 

def driver_fun():
    player_score=0
    comp_score=0
    while(True):
        func_manager.reset_board()               # reseting board at the start of the every game
        game_not_ended=True
        while game_not_ended:
            # Taking Vlaue of row and column in range [0,2]
            cor_in1=0
            while(cor_in1==0):
                user_row=func_manager.user_input_row()
                if(user_row<1 or user_row>3):
                    print("Out of Range value! please enter value in range")
                else:
                    cor_in1=1
                  
                    
            cor_in2=0     
            while(cor_in2==0):
                user_col=func_manager.user_input_col()
                if(user_col<1 or user_col>3):
                    print("Out of Range value! please enter value in range")
                else:
                    cor_in2=1  
                    
            os.system('cls')
            comp_col=func_manager.randomise_comp_col(func_manager.board)
            comp_row=func_manager.randomise_comp_row(func_manager.board)       
            
            # Filling Board only on spaces balnk....
            
            f= func_manager.check_blankspace(func_manager.board,user_row,user_col)
                    
            if(f!=-1):  
                comp_flag=0
                while(comp_flag!=1):
                    if(comp_row==-1 and comp_col==-1):
                        break      
                    elif(func_manager.board[comp_row][comp_col]!="➖"):
                        comp_col=func_manager.randomise_comp_col(func_manager.board)
                        comp_row=func_manager.randomise_comp_row(func_manager.board)
                    else:
                        func_manager.board[comp_row][comp_col]="❌"
                        comp_flag=1 
                            
            # Checking Whether a result occured in the game
                    
                gameflag=func_manager.checkifwin(func_manager.board)
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
                    
                func_manager.print_board()   
                
        ch=input("Want to play again(y/n)?") 
        if(ch!='y'):
            print(f"Final Scores are....PLAYER: {player_score}\tCOMPUTER: {comp_score}")
            break   

if __name__=="__main__":
    print("Hello Welcome to the game of TIC TAC TOE... You will go first\nYou are ⭕ and Computer is ❌\nhere you go...\nEnter The value of Row and column Where you want to Enter your response\nValue of Row and column entered must be in range [1,3]")            
    driver_fun()                      