# Python program to print mirrored hollow rhombus pattern

n=int(input("Enter the number of rows: "))
itr=0
for r in range(0,n):
    itr=itr+1
    for s in range(0,r):
        print(" ",end="")
    for j in range(0,n):
        if(itr==1 or itr==n):
            print("*",end="")
        else:
            if(j==0 or j==n-1):    
                print("*",end="")
            else:
                print(" ",end="")    
    print("")        