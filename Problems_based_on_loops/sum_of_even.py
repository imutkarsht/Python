#python program to print sum of even numbers between 1 to n
n=int(input("Enter thye value of N: "))
s=0
for i in range(1,n+1):
    if(i%2==0):
        # print(i, end=" ")
        s=s+i
print("The Value of the sum is: ",s )        