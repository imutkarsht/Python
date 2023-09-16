import random
from os import system
# Define card values as a dictionary for easier handling of face cards
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def generate_player_card():
    return random.choice(list(card_values.keys()))

def generate_comp_card():
    return random.choice(list(card_values.keys()))

def main():
    player_sum = 0
    Player_list = []
    
    # Generating two cards for the player
    for _ in range(2):
        pc = generate_player_card()
        Player_list.append(pc)
        player_sum += card_values[pc]
    
    comp_sum = card_values[generate_comp_card()]
    print(f"The sum value of the computer is {comp_sum}")

    while player_sum <= 21:
        print(f"Your total sum adds up to {player_sum}")
        choice = input("Would you like to draw another card? (y/n): ")
        
        if choice == 'y':
            pc = generate_player_card()
            Player_list.append(pc)
            player_sum += card_values[pc]
            
            if pc == 'A' and player_sum > 21:
                # If the player drew an Ace and exceeded 21, change its value to 1
                player_sum -= 10
                
            if player_sum > 21:
                return 0
        else:
            while comp_sum < 17:
                cc = generate_comp_card()
                comp_sum += card_values[cc]
                
            print(f"The computer's sum value is {comp_sum}")
            
            if comp_sum > 21 or player_sum > comp_sum:
                return 1
            elif player_sum == comp_sum:
                return -1
            else:
                return 0

if __name__ == "__main__":
    while True:
        ch = input("Would you like to play? (y/n): ").lower()
        system("cls")
        
        if ch != 'n':
            result = main()
            if result == 0:
                print("You lose")
            elif result == -1:
                print("It's a draw")
            else:
                print("You won")
        else:
            break