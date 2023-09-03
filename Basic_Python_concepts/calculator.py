#Python program to make a basic function calculator
print("Enter The numbers: ")
a= int(input("Enter the first number: " ))
b= int(input("Enter the second number: "))

print("Enter The operation you want to perform on these numbers:\n '+' for addition\n '-' for subtraction\n '*' for multiplication\n '/' for division\n '//' for floor division\n '%' for remainder")

c=str(input())

match c:
    case '+':
        print("The sum of numbers is: ", a+b)
    case '-':
        print("The difference of numbers is: ", a-b)
    case '*':
        print("The product of numbers is: ", a*b)
    case '/':
        print("The division of numbers is: ", a/b)
    case '//':
        print("The floor division of numbers is: ", a//b)
    case '%':
        print("The remainder of numbers when divided is: ", a%b)
    case _:
        print("Please Enter the operation correctly.......")     