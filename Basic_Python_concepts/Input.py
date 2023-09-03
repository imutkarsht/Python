#program to demonstrate taking input from user in python

a= input()   #simplest way to take input
print(a)

b=input("Enter your name:")   #taking input with a message
print("My name is", b)

# By default if no type is mention input() consider all inputs as string

x= input("Enter first number: ")
y= input("Enter second number: ")

print(x+y) 
print(int(x)+int(y))