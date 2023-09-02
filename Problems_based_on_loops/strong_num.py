# Python program to check if a number is strong or not

num=int(input("Enter the number: "))
n1=num
def fact(num):
    p=1
    while(num!=0):
        p=p*num
        num=num-1
    return p  

sum=0
while(num!=0):
    tmp=int(num%10)
    sum=sum+ fact(tmp)
    num=int(num/10)
if(sum==n1):
    print("Number is strong: ")
else:
    print("Number is not strong: ")    
    
      