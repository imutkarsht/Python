# python program to print all perfect numbers upto n

n=int(input("Enter the Number upto which you want to print: "))

def perfect(i):
    num=i
    sum=0
    for j in range(1,i):
        if(i%j==0):
            sum=sum+j
    if(sum==num):
        return True
    else:
        return False
    
           
for i in range(1,n+1):
    if(perfect(i)==True):
        print(i,end=" ")     