#python program to check if a number is prime

num=int(input("Enter the Number: "))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count=count+1

if(count==2):
    print("The Entered number is a prime: ")
else:
    print("The entered number is not prime: ")            