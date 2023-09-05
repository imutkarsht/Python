# Write a python program to check a given list (length will be at least 2) of integers
# and return true if there are two values 15, 15 next to each other.

def init_list(List,size):
    for i in range(size):
        b=int(input(f"Enter element no {i+1} "))
        List.append(b)
        
list=[]

size=int(input("Enter the size of List you want to create(size>=2): "))
init_list(list,size)    

num=int(input("Enter the number you want to check if they are consequent positions..."))

flag=0

for i in range(0,size):
    if(i<size-1):
        if(list[i]==list[i+1]):
            flag=-1

if(flag==0):
    print("False")
else:
    print("True")            
      