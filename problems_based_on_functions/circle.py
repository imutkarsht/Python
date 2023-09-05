# Python program to find Diameter, circumference and area of a circle using function

r=int(input("Enter the Value of radius: "))

def fun(r):
    print("The value of Diameter is: ", 2*r)
    print("The value of circumference is: ", 2*(3.14)*r)
    print("The value of area is: ", (3.14)*r*r)
    
fun(r)    