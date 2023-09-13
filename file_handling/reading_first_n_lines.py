# Python program to read first n line of a file

n=int(input("Enter the value of N "))
f=open("D:/Coding/Python/file_handling/evenodd.txt",'r')
while(n!=0):
    print(f.readline(),end="")
    n-=1
f.close()    