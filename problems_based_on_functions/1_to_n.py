u=int(input("Enter the value of upperlimit: "))
l=int(input("Enter the value of lowerlimit: "))


def upton(l,u):
    if(l>u):
        return
   
    print(l, end=" ")
    upton(l+1,u)    

upton(l,u)    