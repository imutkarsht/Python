# Python program to print mirrored rhombus pattern

n=int(input("Enter the number of rows: "))
for r in range(0,n):
    for s in range(0,r):
        print(" ",end="")
    for j in range(0,n):
        print("*",end="")
    print("")        