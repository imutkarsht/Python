# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new
# list should contain odd numbers from the first list and even numbers from the second list.
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# result list: [25, 35, 40, 60, 90]
import os

n1=int(input("Enter the size of first list: "))
n2=int(input("Enter the size of second list: "))

list1=[]  
list2=[]
new_list=[]

def init_list(List,size):
    for i in range(size):
        b=int(input(f"Enter element no {i+1} "))
        List.append(b)
        
init_list(list1,n1)
init_list(list2,n2)
    
def create_new_list(old_list1,old_list2,new_list):

    for i in range(n1):
        if(old_list1[i]%2!=0):
            b=old_list1[i]
            new_list.append(b)    

    for j in range(n2):
        if(old_list2[j]%2==0):
            b=old_list2[j]
            new_list.append(b)    
            
create_new_list(list1,list2,new_list)       
                 
os.system('cls') 

print("The List 1: ",list1)
print("The List 2: ",list2)
print("The new list: ",new_list)  