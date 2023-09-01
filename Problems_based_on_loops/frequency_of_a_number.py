# Python Program to find the frequency of a number in given integer

n=int(input("Enter The number: "))
d=int(input("Enter The digit of which frequency you want to find: "))

num=n
count=0
    
while(n!=0):
    tmp=int(n%10)
    if(tmp==d):
        count=count+1
    n=int(n/10)

    
print("The digit ",d, " has appeared ",count," times in given number ",num)           