# python program to print pyramid pattern
n= int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,(2*i)+1):
        print("*",end="")
    print("")        