a=input("Enter the number: ")
print(f"Multiplication Table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")

#Instead of Throwing error this message will be executed..
        
except ValueError :
    print("invalid input...Try Entering an integer")

# These codes will execute normally...
    
print("Some lines of code")
print("End of program")            