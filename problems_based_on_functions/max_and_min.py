# Python program to find max and min between two numbers using python

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

def maxmin(a,b):
    if(a>b):
        print("Max= ",a)
        print("Min= ",b)
    elif(a<b):
        print("Max= ",b)
        print("Min= ",a)
    else:
        print("Both numbers are equal:")    
        
maxmin(a,b)        