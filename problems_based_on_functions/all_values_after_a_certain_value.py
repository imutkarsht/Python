# program to create a new list taking the elements before the element value 
# key from a given list of integers.

import os
n1=int(input("Enter the size of orignal list: "))
key=int(input("Enter the value after whicch you want to get all new elements in list: "))
list1=[] 
newlist=[]

def init_list(List,size):
    for i in range(size):
        b=int(input(f"Enter element no {i+1} "))
        List.append(b)
        
init_list(list1,n1)
def create_new_list(old_list,new_list,size,key):
    for i in range(0,size):
        if(old_list[i]==key):
            for j in range(i+1,size):
                b=old_list[j]
                new_list.append(b)
        else:
            continue
        
create_new_list(list1,newlist,n1,key)            

os.system('cls')

print("The old list: ", list1)                   
print("The new list: ", newlist)                  