#python program to find all prime factors of a number

num=int(input('Enter The number: '))
for i in range(1,num+1):
    if(num%i==0):
        count=0
        for j in range(1,i+1):
            if(i%j==0):
                count=count+1
        if(count==2):
            print(i,end=" ")        
