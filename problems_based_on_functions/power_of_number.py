n=int(input("Enter the number: "))
p= int(input("Enter the power upto which you want to raise it: "))

def powerofno(n,p):
    if(p==0):
        return 1
    elif(p> 0):
        return n * powerofno(n, p - 1)
    else:
        return 1 / powerofno(n, -p)
    
print(powerofno(n,p))    