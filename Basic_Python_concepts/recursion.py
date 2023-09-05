# Python program to demonstrate recursion in Python

# factorial...
# factorial(n)= n * factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))    

# 3 * factorial(2)        ---> 6  --> Our answer
       # 2 * factorial(1) ---> 2
            #   1* 1      ---> 1