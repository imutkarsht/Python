#Python program to count number of digits in a number

n=int(input("enter the number: "))
c=0
while(n!=0):
    n=n//10
    c=c+1
    
print("The entered number has ", c ," digits")    