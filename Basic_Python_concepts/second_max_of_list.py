if __name__ == '__main__':
    arr=[]
    n = int(input())
    if(n>=2):    
    
        for i in range(0,n):
            b=int(input())
            arr.append(b)
        
        
    # arr = map(int, input().split())
        max=0
        for i in range(n):
            if(arr[i]>max):
                max=arr[i]
        second_max=0        
        for j in range(n):
            if(arr[j]>second_max and arr[j]<max):
                second_max=arr[j]
    
        print(second_max) 
        
    else:
        print("value of N must be > 2")    