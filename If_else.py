#python program to demonstrate use of conditional statements ( if, if-else, elif)

a=int(input("Enter your age: "))
print("your age is, ", a)

# here if block will check if the entered value of a is > 18 or not in case it is true
# if block will be executed, otherwise else block will be executed( if given)
# if block only executes if given condition with if results into a true boolean value

if(a>18):
    print("you can drive")     #The space before print() is called indentation, it is necessary and tells interpreter that we are in if block
else:
    print("you can't drive")    
print("It's not the part of else block and will get executed regardless condition in if")