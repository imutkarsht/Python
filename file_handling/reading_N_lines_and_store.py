# Python program to read n line of a file and store it into a list

n=int(input("Enter the value of N "))
f=open("D:/Coding/Python/file_handling/evenodd.txt",'r')
list=[]
i=0
while(n!=0):
    list+=f.readline().strip("\n")
    i+=1
    n-=1
print(list)    
f.close()   