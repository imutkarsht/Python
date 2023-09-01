#python program to print odd numbers between 1 to n
n=int(input("Enter thye value of N: "))
i=1
while(i<n):
    if(i%2!=0):
        print(i, end=" ")
    i=i+1
    