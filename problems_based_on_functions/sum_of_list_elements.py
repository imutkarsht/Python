# Python Program to find sum of  element of a list using function(recursions)

n=int(input("Enter the size of the list: "))
arr=[]
for i in range(0,n):
    b=int(input("Enter element no "))
    arr.append(b)
    
def findsum(arr,n):
    if(n==0):
        return n
    else:
        return arr[n-1]+findsum(arr,n-1)   
    
print(findsum(arr,n))     