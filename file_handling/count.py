# Python Program to count no of lines, words and characters in a txt file

f = open("D:/Coding/Python/file_handling/count.txt", mode="r")
num_lines = 0
num_char = 0
num_words = 0

for line in f:
    num_lines += 1
    line = line.strip("\n")
    num_char += len(line)
    list1 = line.split()
    num_words += len(list1)
f.close()

print("Number of lines = ", num_lines)
print("Number of characters = ", num_char)
print("Number of words = ", num_words)