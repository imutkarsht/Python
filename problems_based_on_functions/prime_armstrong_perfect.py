# pythn program to check if a number is prime, armstrong or perfect
import math
n= int(input('Enter the number: '))

def isprime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print("The number Entered is a prime number")
    else:
        print("The number Entered is not a prime number")
        

def no_of_dig(n):
    c=0
    while(n!=0):
        n=n//10
        c=c+1
    return c
    
def isarmstrong(n):
    c=no_of_dig(n)
    num=n
    sum=0
    while(n!=0):
        tmp=int(n%10)
        sum=sum+math.pow(tmp,c)
        n=int(n/10)
    if(num==sum):    
        print("The Number Entered is an Armstrong number: ")
    else:
        print("The Number Entered is not an Armstrong number: ")
        
def isperfect(n):
    num=n
    sum=0
    for i in range(1,num):
        if(num%i==0):
         sum=sum+i

    if(sum==n):
        print("The Number entered is a perfect number:")
    else:
        print("The number entered  is not a perfect no:")    
        
isprime(n)
isarmstrong(n)
isperfect(n)       
                     
                        