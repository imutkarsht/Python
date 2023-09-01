#python program to find GCD(HCF) of Two numbers

#input two numbers from user. Store them in some variable
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

# Declare and initialize a variable to hold hcf
hcf=1

# Find minimum between the given two numbers. Store the result in some variable say

if(n1>n2):
    min=n2
else:
    min=n2
# Run a loop from 1 to min, increment loop by 1 in each iteration

for i in range(1,min+1):
# Inside the loop check if i is a factor of two numbers i.e. 
# if i exactly divides the given two numbers n1 and n2 then set i as HCF    
    if(n1%i==0 and n2%i==0):
        hcf=i       
 
print("The hcf of two numbers given is: ", hcf)