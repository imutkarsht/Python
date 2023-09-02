# python program to print fibbonacci series upto n

n=int(input("Enter the number of terms upto which you want to get the series "))

first=0
second=1

print("0 1",end=" ")

for i in range(3,n+1):
    third=first+second
    print(third,end=" ")
    first=second
    second=third    