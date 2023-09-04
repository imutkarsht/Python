# python program to print hollow mirrored right angle triangle pattern
itr=0
n= int(input("Enter The number of rows: "))
for i in range(0,n):
    itr=itr+1
    s=n-i+1
    while(s!=0):
        print(" ",end="")
        s=s-1
    for j in range(0,i+1):
        if(itr==1 or itr==n):
            print("*",end="")
        else:
            if(j==0 or j==i):                   
                print("*",end="")
            else:
                print(" ", end="")    
    print("")    