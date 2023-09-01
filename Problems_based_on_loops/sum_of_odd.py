#python program to print sum of odd numbers between 1 to n
n=int(input("Enter thye value of N: "))
s=0
i=1
while(i<n):
    if(i%2!=0):
        # print(i, end=" ")
        s=s+i
    i=i+1
print("The value of the sum is: ", s)    