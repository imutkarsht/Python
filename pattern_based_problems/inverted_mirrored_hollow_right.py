# python program to print mirrored inverted hollow right triangle

n= int(input("Enter the number of rows: "))
itr=0
for i in reversed(range(0,n)):
    s=0
    s=n-i+1
    itr=itr+1
    while(s!=0):
        print(" ",end="")
        s=s-1
        
    if(n%2==0):
        for j in reversed(range(0,i+1)):
            if(itr==1 or itr==i+1):
                print("*",end="")
            else:
                if(j==0 or j==i):    
                    print("*",end="")
                else:
                    print(" ", end="")
        print("") 
    else:
        for j in reversed(range(0,i+1)):
            if(itr==1 or itr==i+2):
                print("*",end="")
            else:
                if(j==0 or j==i):    
                    print("*",end="")
                else:
                    print(" ", end="")
        print("")                           