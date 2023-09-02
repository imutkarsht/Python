# Python program to check if a number is perfect or not

num=int(input('Enter The number: '))
n=num
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i

if(sum==n):
    print("The Number is perfect:")
else:
    print("The number is not perfect:")            
        