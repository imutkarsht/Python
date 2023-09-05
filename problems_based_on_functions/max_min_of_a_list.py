# Python Program to find max and min element of a list using functions

n=int(input("Enter the size of the list: "))
arr=[]
for i in range(0,n):
    b=int(input("Enter element no "))
    arr.append(b)
    
def max_list(arr,n):
    max=0
    for i in range(0,n):
        if(arr[i]>max):
            max=arr[i]
    print("The maximum value of list is: ", max)
    
def min_list(arr,n):
    min=arr[0]
    for i in range(0,n):
        if(arr[i]<min):
            min=arr[i]
    print("The min value of the list is: ",min)                        
    
max_list(arr,n)
min_list(arr,n)