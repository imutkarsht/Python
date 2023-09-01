#python program to find factors of a number

num=int(input('Enter The number: '))
for i in range(1,num+1):
    if(num%i==0):
        print(i, end=" ")
        