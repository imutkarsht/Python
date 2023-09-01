#python program to calculate factorial of a number
num=int(input('Enter The number: '))
p=1
while(num!=0):
    p=p*num
    num=num-1
    
print("The value of the factorial is: ", p)    