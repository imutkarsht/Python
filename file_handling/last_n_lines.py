# Python program to read last n line of a file

n = int(input("Enter the value of N "))
f = open("D:/Coding/Python/file_handling/evenodd.txt", "r")

# 1. Find Number of lines in the file
num_of_lines = 0
for line in f:
    num_of_lines += 1

# 2. Return file pointer at starting position

f.seek(0)

# 3. Find number of line from where you have to start

net_line = num_of_lines - n

# 4. Send file pointer to end iof net_line

while net_line != 0:
    f.readline()
    net_line -= 1

# 5. Print Number of lines you want from there

while n != 0:
    print(f.readline(), end="")
    n = n - 1
f.close()
