# Python program to print first and last digit of an entered number

n=int(input("enter the number: "))
ch=str(n)    
c=0
while(n!=0):
    n=n//10
    c=c+1
print("The first digit is: ", ch[0] )
print("The last digit is: ", ch[c-1])    