# python program to print mirrored inverted right triangle

n= int(input("Enter the number of rows: "))
for i in reversed(range(0,n)):
    s=0
    s=n-i+1
    while(s!=0):
        print(" ",end="")
        s=s-1
        
    for j in reversed(range(0,i+1)):
        print("*",end="")
    print("")            