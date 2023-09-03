#program to check greater of three numbers using if else

print("Enter Three numbers: ")
a=int(input())
b=int(input())
c=int(input())

if(a>=b)and(a>=c):
    print("The Greatest of three numbers is: ", a)
elif(b>=a) and( b>=c):
    print("The greatest of three numbers is: ", b)
else:
    print("The greatest of three numbers is: ", c)            