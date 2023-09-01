#python program to print even numbers between 1 to n
n=int(input("Enter thye value of N: "))
for i in range(1,n+1):
    if(i%2==0):
        print(i, end=" ")
        