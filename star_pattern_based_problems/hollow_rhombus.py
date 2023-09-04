# Python program to print hollow rhombus pattern
itr=0
n=int(input("Enter the number of rows: "))
for r in range(0,n):
    s=n-r-1
    itr=itr+1
    while(s>0):
        print(" ", end="")
        s=s-1
    for j in range(0,n):
        if(itr==1 or itr==n):
            print("*",end="")
        else:
            if(j==0 or j==n-1):
                print("*",end="")
            else:
                print(" ",end="")        
    print("")        