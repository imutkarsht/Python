import random
import os

words = [
    "absurd",
    "zombie",
    "transcript",
    "buffalo",
    "jazz",
    "quartz",
    "breeze",
    "puzzle",
    "dazzle",
    "fuzzy",
    "jigsaw",
    "zigzag",
    "buzzing",
    "glowing",
    "mystery",
    "victory",
    "gizmo",
    "hijack",
    "jungle",
    "kayak",
    "muffin",
    "oxygen",
    "pixel",
    "quiver",
    "rhythm",
    "sphinx",
    "vortex",
    "wizard",
    "xylophone",
    "yacht",
    "zeppelin",
]
HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def str_to_list(random_word):
    word_as_list = list(random_word)
    return word_as_list


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


def input_guess():
    while True:
        guess = input("Guess a letter....")
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Please Enter a valid input...")
            continue


def check_word(word):
    if "-" in word:
        return 0
    return 1


def fill_guess(guess, b_word, normal_word):
    b_word_list = list(b_word)
    for i in range(len(normal_word)):
        if normal_word[i] == guess:
            b_word_list[i] = guess
    return "".join(b_word_list)


def check_guess(guess, normal_word, b_word):
    if guess in normal_word:
        b_word = fill_guess(guess, b_word, normal_word)
        if check_word(b_word) == 1:
            return 1
        return b_word
    else:
        return -1


def main(random_word):
    i = 0
    str_as_list = str_to_list(random_word)
    word = blank_generator(str_as_list)
    while True:
        print(
            "WELCOME TO THE GAME OF HANGMAN\n\nFILL THE GIVEN WORD BY GUESSING BLANKS CORRECTLY, OR THIS MAN WOULD BE HANGED SAVE HIM...."
        )
        print("\nTHE WORD IS....\n")
        print(word)
        guess = input_guess()
        a = check_guess(guess, str_as_list, word)

        if a == 1:
            print("You won and saved the life of man...")
            return

        elif a == -1:
            os.system(
                "cls" if os.name == "nt" else "clear"
            )  # Clear the terminal screen
            print("Your Guess was Incorrect... you lost one life")
            i += 1
            if i == len(HANGMANPICS):
                print("YOU LOSE MAN HAS BEEN HANGED!")
                print(HANGMANPICS[i - 1])
                return
            else:
                os.system(
                    "cls" if os.name == "nt" else "clear"
                )  # Clear the terminal screen
                print(f"You have {len(HANGMANPICS) - i} lives left....")
                print(HANGMANPICS[i - 1])

        else:
            os.system(
                "cls" if os.name == "nt" else "clear"
            )  # Clear the terminal screen
            word = a


if __name__ == "__main__":
    random_word = random.choice(words)
    main(random_word)
