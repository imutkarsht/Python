r=int(input("Enter the Number of Rows: "))
c=int(input("Enter the Number of columns: "))
for i in range(r):
    for j in range(c):
        if(i==0 or i==r-1):
            print("*", end="")
        else:
            if(j==0 or j==c-1):
                print("*",end="")  
            else:
                print(" ", end="")   
    print("")               