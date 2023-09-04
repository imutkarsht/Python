# python program to print mirrored right angle triangle pattern

n= int(input("Enter The number of rows: "))
for i in range(0,n):
    s=n-i+1
    while(s!=0):
        print(" ",end="")
        s=s-1
    for j in range(0,i+1):
        print("*",end="")
    print("")    