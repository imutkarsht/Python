# Python program to check if entered number is a palindrome
import math
n=int(input("Enter a number: "))
num=n

#Finding number of digits

c=0
while(n!=0):
    n=n//10
    c=c+1
       
digits=c    

# Logic to reverse the given number
s=0
orignal_number=num
while(digits!=0):
    tmp=int(num%10)
    s=int(s+tmp*math.pow(10,digits-1))
    num=int(num/10)
    digits=digits-1
    
if(s==orignal_number):
    print("The Entered Number is a Palindrome:")
else:
    print("The Entered Number is not a palindrome:")        
    