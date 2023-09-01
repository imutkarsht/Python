# Python Program to get a number and return it's reverse

import math
n=int(input("Enter a number: "))
num=n

#Finding number of digits

c=0
while(n!=0):
    n=n//10
    c=c+1
       
digits=c    
s=0
while(digits!=0):
    tmp=int(num%10)
    s=int(s+tmp*math.pow(10,digits-1))
    num=int(num/10)
    digits=digits-1
    
print("The number after being reversed is:", s)    