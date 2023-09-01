#python program to find LCM of Two numbers

#input two numbers from user. Store them in some variable
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

if(n1>n2):
    max=n1
else:
    max=n2    
    
lcm=1
i=max    
while(True):
    if((i%n1==0) and (i%n2==0)):
        lcm=i
        break
    else:
        i=i+max

print("The value of LCM is", i)              