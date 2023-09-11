import random
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Function to select a list of word based on difficulty selected by player

def difficulty_level():
    while True:
        ch=int(input("Select the Dificulty level\n1.Easy\n2.Medium\n3.hard\n"))
        match ch:
            case 1: 
                words = [
                "apple", "beach", "chair", "dance", "eleven", "fruits", "giant", "happy", "igloo",
                "jacket", "kite", "lemon", "music", "ocean", "piano", "queen", "rabbit", "sunny", "tiger",
                "umbrella", "violet", "waffle", "yellow", "zebra"]
            
                return words
            
            case 2:
                words = [
                "cabin", "dolphin", "forest", "guitar", "jungle", "laptop", "monkey", "puzzle",
                "sunset", "toucan", "vampire", "wonder", "yellow", "zebra", "sphinx", "quartz",
                "jigsaw", "flavor", "expert", "buffet", "cipher", "coyote", "hybrid", "oxygen",
                "whale", "vortex", "anxious", "curious", "melody", "mosaic", "organic", "temple"]
                
                return words
            
            case 3:
                words = [
                "abyss", "awkward", "cryptic", "gazebo", "jazzed", "jigsaw", "labyrinth", "lynx",
                "mystify", "oxygen", "pajama", "psyche", "rhythm", "sphinx", "syndrome", "voodoo",
                "whiskey", "xylophone", "zeppelin", "zephyr", "zigzag", "zombie", "vortex", "quartz"]
                
                return words
            case _ :
                print("Please Enter a valid Input")
                
# Function to convert a string to list

def str_to_list(random_word):
    word_as_list = list(random_word)
    return word_as_list

# function to generate blank spaces in the word randomly selected

def blank_generator(word_as_list):
    word_with_blanks = list(word_as_list)
    for i in range(0, len(word_as_list) - 3):
        while True:
            random_index = random.randint(0, len(word_as_list) - 1)
            if word_with_blanks[random_index] != "-":
                word_with_blanks[random_index] = "-"
                break

    blank_word = "".join(word_with_blanks)
    return blank_word

# Function to take guess of player as Input

def input_guess():
    while True:
        guess = input("Guess a letter....").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Please Enter a valid input...")
            continue
# Function to check if there is any blank space left in the word

def check_word(word):
    if "-" in word:
        return 0
    return 1

# Function to fill _ when guess made by player is correct

def fill_guess(guess, b_word, normal_word):
    b_word_list = list(b_word)
    for i in range(len(normal_word)):
        if normal_word[i] == guess:
            b_word_list[i] = guess
    return "".join(b_word_list)

# Function to check if guess made by player was correct 
def check_guess(guess, normal_word, b_word):
    if guess in normal_word:
        b_word = fill_guess(guess, b_word, normal_word)
        if check_word(b_word) == 1:
            return 1
        return b_word
    else:
        return -1
# Main Driver function of the program

def main(random_word):
    i = 0
    str_as_list = str_to_list(random_word)
    word = blank_generator(str_as_list)
    while True:
        print("WELCOME TO THE GAME OF HANGMAN\n\nFILL THE GIVEN WORD BY GUESSING BLANKS CORRECTLY, OR THIS MAN WOULD BE HANGED SAVE HIM....")
        print("\nTHE WORD IS....\n")
        print(word)
        guess = input_guess()
        a = check_guess(guess, str_as_list, word)

        if a == 1:
            print("You won and saved the life of man...")
            return

        elif a == -1:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            print("Your Guess was Incorrect... you lost one life")
            i += 1
            if i == len(HANGMANPICS):
                print("YOU LOSE MAN HAS BEEN HANGED!")
                print(HANGMANPICS[i-1])
                print(f"\nThe correct word was {random_word}")
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print(f"You have {len(HANGMANPICS) - i} lives left....")
                print(HANGMANPICS[i - 1])

        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
            word = a