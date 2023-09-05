# python program to print inverted hollow right angle triangle
itr=0
n= int(input("Enter the number of rows: "))
for i in reversed(range(0,n)):
    itr=itr+1
    if(n%2==0):
        for j in reversed(range(0,i+1)):
            if(itr==1 or itr==i+1):
                print("*",end="")
            else:
                if(j==0 or j==i):
                    print("*",end="")    
                else:    
                 print(" ",end="")
        print("")    
        
    else:
        for j in reversed(range(0,i+1)):
            if(itr==1 or itr==i+2):
                print("*",end="")
            else:
                if(j==0 or j==i):
                    print("*",end="")    
                else:    
                 print(" ",end="")
        print("")    