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
            user_row,user_col=func_manager.user_input()
                    
            os.system('cls')
            comp_col=func_manager.randomise_comp_col()
            comp_row=func_manager.randomise_comp_row()       
            
            # Filling Board only on spaces balnk....
            
            f= func_manager.check_blankspace(func_manager.board,user_row,user_col)
                    
            if(f!=-1):  
                comp_flag=0
                while(comp_flag!=1):
                    if(comp_row==-1 and comp_col==-1):
                        break      
                    elif(func_manager.board[comp_row][comp_col]!="➖"):
                        comp_col=func_manager.randomise_comp_col()
                        comp_row=func_manager.randomise_comp_row()
                    else:
                        func_manager.board[comp_row][comp_col]=func_manager.COMP_RESPONSE
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
            print(f"\nFinal Scores are....PLAYER: {player_score}\tCOMPUTER: {comp_score}")
            break   

if __name__=="__main__":
    print(f"Hello Welcome to the game of TIC TAC TOE... You will go first\n\nYou are {func_manager.PLAYER_RESPONSE} and Computer is {func_manager.COMP_RESPONSE}\n\nhere you go...\n\nEnter The value of Row and column Where you want to Enter your response\n\nValue of Row and column entered must be in range [1,3]\n")            
    driver_fun()                      