#python program to print sum of all prime upto n

n=int(input("Enter The Number upto which you want to get prime sum: "))
sum=0
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        sum=sum+i
        
print("The sum is: ", sum)            