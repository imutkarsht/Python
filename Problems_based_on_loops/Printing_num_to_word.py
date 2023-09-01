# Python progrAM TO print an entered number in words
import math
n=int(input("Enter the number: "))
num=n

c=0
while(n!=0):
    n=n//10
    c=c+1
    
    
while(num!=0):
    tmp=int(num//math.pow(10,c))
    match tmp:
        case 0:
            print("zero",end=" ")
        case 1:
            print("one",end=" ")
        case 2:
            print("two",end=" ")
        case 3:
            print("three",end=" ")
        case 4:
            print("four",end=" ")
        case 5:
            print("five",end=" ")
        case 6:
            print("six",end=" ")
        case 7:
            print("seven",end=" ")
        case 8:
            print("eight",end=" ")
        case 9:
            print("nine",end=" ")
        case _:
            print("Error")    
            
    num=int(num%math.pow(10,c))      
    c=c-1  