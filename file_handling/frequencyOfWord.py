# Python program to check how many times a particular word has apppeared in a file

f = open("D:/Coding/Python/file_handling/frequencyofWord.txt")
word = []
word += f.readline().split(" ")
f.close()
flag = 0
key = input("Enter the Word you want to check for ")

for w in word:
    if w == key:
        flag += 1

print(f"\nThe word {key} appeared {flag} times in file")