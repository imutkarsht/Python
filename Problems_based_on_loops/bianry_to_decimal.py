# Python Program to convert a given binary number into decimal
import math
binary=str(input("Enter the binary number: "))
sum=0
for i in range(0,len(binary)):
    sum=sum+(int(binary[-(i+1)])*math.pow(2,i))    
    
print("The decimal equivalent of binary is: ", int(sum))      