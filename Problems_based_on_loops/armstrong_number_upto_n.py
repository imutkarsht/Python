# Python Program to print all armstrong numbers upto n

import math
n=int(input("enter the number upto which you want to print armstrong numbers: "))

def no_of_dig(i):
    c=0
    while(i!=0):
        i=i//10
        c=c+1
    return c

def armstrong(i,d):
    sum=0
    n1=i
    while(i!=0):
        tmp=int(i%10)
        sum=sum+math.pow(tmp,d)
        i=int(i/10)
    if(n1==sum):
        return True
    else:
        return False
        
for i in range(1,n+1):
    if (armstrong(i,no_of_dig(i))==True):
         print(i, end=" ")
        