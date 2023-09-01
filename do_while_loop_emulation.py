# Python code to demonstrate do while loop
# Do while loop
# Do while loop is a type of control looping statement that can run any statement 
# until the condition statement becomes false specified in the loop. In do while
# loop the statement runs at least once no matter whether the condition is false or true.

# by default do while loops are not there in python and we have to emulate them

# The most common technique to emulate a do-while loop in Python is to use an infinite 
# while loop with a break statement wrapped in an if statement that checks a given condition
# and breaks the iteration if that condition becomes true:


while True:
    i=int(input("Enter The positive number: "))
    print(i)
    if(not i>0):
        break