import driver_func as df
import random

if __name__ == "__main__":
    while True:
        words=df.difficulty_level()
        random_word = random.choice(words)
        df.main(random_word)
        ch=input("Want to play again(y/n)?")
        if(ch!='y'):
            break