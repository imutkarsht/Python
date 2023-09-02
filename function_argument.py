# There are Four type of argument we can provide in functions...
# 1. default argument

def average(a=9,b=1):
    print("Average is: ", (a+b)/2)
    
average()      #will work on default 9,1
average(2)     # value of a will changed to 2 and default value of b will be taken
average(3,5)   # default values will be replaced with 3 and 5    

# 2. Keyword Arguments

average(b=9)   #arguments are provided with key values and order won't matter

# 3. required Argument 
       # argument must necessarily be passed
       
# 4. Variable length argument

def avg(* numbers):            # It will take numbers as tuples
    sum=0
    for i in numbers:
        sum=sum+i   
    print("Average is: ", sum/len(numbers))
    
 
avg(5,6,7,1)
avg(2,4)   