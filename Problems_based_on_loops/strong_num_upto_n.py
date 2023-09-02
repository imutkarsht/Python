# python program to print all strong numbers upto n

n=int(input("Enter the Number upto which you want to print: "))

def fact(num):
    p=1
    while(num!=0):
        p=p*num
        num=num-1
    return p  

def strong(i):
    num=i
    sum=0
    while(i!=0):
        tmp=int(i%10)
        sum=sum+ fact(tmp)
        i=int(i/10)
    if(sum==num):
        return True
    else:
        return False
        
    
           
for i in range(1,n+1):
    if(strong(i)==True):
        print(i,end=" ")  