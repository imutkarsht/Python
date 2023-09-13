#Python program to read a file and check whether numbers written in it are even or odd and sepearte them
f=open("D:/Coding/Python/file_handling/evenodd.txt",'r')
a=f.read().split("\n")
print(a)
for num in a:
    if int(num)%2==0:
        f1=open("D:/Coding/Python/file_handling/even.txt",'a')
        f1.write(str(num))
        f1.write("\n")
    else:
       f2=open("D:/Coding/Python/file_handling/odd.txt",'a')
       f2.write(str(num))
       f2.write("\n")
            
f1.close() 
f2.close()       