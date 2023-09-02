# Python program to check if a given number is armstrong or not...
import math
n=int(input("enter the number: "))
num=n
n1=n

def no_of_dig(n):
    c=0
    while(n!=0):
        n=n//10
        c=c+1
    return c

dig=no_of_dig(n)
sum=0
while(num!=0):
    tmp=int(num%10)
    sum=sum+math.pow(tmp,dig)
    num=int(num/10)

if(n1==sum):
    print("The Given number is armstrong Number: ")
else:
    print("The given number is not an armstrong number: ")                       