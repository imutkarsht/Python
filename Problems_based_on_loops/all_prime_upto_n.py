# Python Program to print all prime numbers upto n

n=int(input("Enter The Number upto which you want to print prime: "))
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i,end=" ")       