#python program to calculate product of digits of a number
import math

n=int(input("enter the number: "))
num=n
# find number of digits

c=0
while(n!=0):
    n=n//10
    c=c+1

p=1

while(c!=0):
        p=p*(num%10)     # precedence of operator has to be kept in mind otherwise runtime error occurs
        num=int(num/10)
        c=c-1

print("The Product of the digits is:" ,p)        