#program to demonstrate typecasting in python

a="1"
b="2"

print(a+b)

#--> output will be 12 as a and b are string variable here hence a+b will concatenate two strings

print(int(a)+int(b))

#--> output will be 3 as we explicitly converted a and b into integers


#implicit Type casting....

c=1.9
d=8

print(c+d)

#--> output will be 9.9 a float as python will automatically convert 8 into a float