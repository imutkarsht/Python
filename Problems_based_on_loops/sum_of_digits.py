#python program to calculate sum of digits of a number
import math

n=int(input("enter the number: "))
num=n
# find number of digits

c=0
while(n!=0):
    n=n//10
    c=c+1

s=0

while(c!=0):
        s=s+num%10
        num=int(num/10)
        c=c-1

print('The Sum of the digits is: ', s)        