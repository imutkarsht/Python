# python program to print right angle triangle pattern

n= int(input("Enter The number of rows: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("")    