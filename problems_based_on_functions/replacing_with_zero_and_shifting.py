# program to create a list after replacing all the values 5 with 0 and shifting all zeros to the right.

import os
n1=int(input("Enter the size of first list: "))
key=int(input("Enter the value you want to get replaced by zero: "))
list1=[] 
newlist=[]

def init_list(List,size):
    for i in range(size):
        b=int(input(f"Enter element no {i+1} "))
        List.append(b)
        
init_list(list1,n1)

def create_new_list(old_list,new_list,size,key):
    for i in range(0,size):
        if(old_list[i]!=key):
            b=old_list[i]
            new_list.append(b)
        else:
            continue
    j=size-len(new_list)
    
    while(j!=0):
        b=0
        new_list.append(b)
        j=j-1
        
create_new_list(list1,newlist,n1,key)

os.system('cls')

print("The old list: ", list1)                   
print("The new list: ", newlist)          
                