# program to create a list from a given list of integers 
# shifting all even numbers before all odd numbers.

import os
n1=int(input("Enter the size of first list: "))
list1=[] 
newlist=[]

def init_list(List,size):
    for i in range(size):
        b=int(input(f"Enter element no {i+1} "))
        List.append(b)
        
init_list(list1,n1)
        
def create_new_list(old_list,new_list,size):
    for i in range(0,size):
        if(old_list[i]%2==0):
            b=old_list[i]
            new_list.append(b)
                   
    for j in range(0,size):
        if(old_list[j]%2!=0):
            b=old_list[j]
            new_list.append(b)
            
create_new_list(list1,newlist,n1)            

os.system('cls')

print("The old list: ", list1)                   
print("The new list: ", newlist)                   