# Python program to print rhombus pattern

n=int(input("Enter the number of rows: "))
for r in range(0,n):
    s=n-r-1
    while(s>0):
        print(" ", end="")
        s=s-1
    for j in range(0,n):
        print("*",end="")
    print("")        