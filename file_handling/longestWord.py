# Python program to find the longest word in a file

f=open("D:/Coding/Python/file_handling/longestWord.txt")
word=[]
word+=f.readlines()
f.close()
longest_word=word[0]

for w in word:
    if(len(longest_word)<len(w)):
        longest_word=w
        
print(longest_word)
