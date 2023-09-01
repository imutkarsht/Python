# Python Program to demonstrate for loops
# loops are used when programmer wants to execute a group of statements a certain number of time

name = "Utkarsh"

# Iterating a string with for loop

for i in name :
    print(i)
    if(i=='a'):
        print("this is first letter of alphabet")
        
# Iterating a list with for loop

colors = ["red","blue","green","yellow"]

for color in colors:
    print("\n") 
    print(color)
    for i in color:            # Nested loop
        print(i, end=" ")       
print("\n")
                               # Range() in for loop

for k in range(10):            # range(10) then it will go from 0 to 9 
    print(k+1, end=" ")
print("\n")    

for j in range(2,10):
                               # range(start, stop , step)
    print(j, end=" ")
print("\n")
    
for l in range(4,10,2):        # it will skip every second iteration
    print(l, end=" ")            