# python program to print inverted right angle triangle

n= int(input("Enter the number of rows: "))
for i in reversed(range(0,n)):
    for j in reversed(range(0,i+1)):
        print("*",end="")
    print("")    