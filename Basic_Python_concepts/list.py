# program to demosntrate Lists in python

# List is used to hold many values under one name

# marks=[18,17,16] 
    
# we can also add other data types to list

marks=[18,17,16,'utkarsh',False, 20,11,19]      # List is ordered collection of data

print(marks[0])                       # will print first value of list
print(marks[1])                       # ...........second.............
print(marks[2])                       # ...........third..............
print(marks[3])                       # ...........fourth..............
print(marks[4])                       # ...........fifth..............

# To check if an item is part of a list or not....

if 'utkarsh' in marks:
    print("yes")
else:
    print("no")    

# we can do same with string

if 'arsh' in 'utkarsh':
    print("yes")
else:
    print("no")
    
# we can also perform slicing to lists

print(marks)            
print(marks[1:7])            
print(marks[1:7:2])            

# list comprehension ---> creating a list on fly

lst= [i*i for i in range(10)]
print(lst)

lst= [i*i for i in range(10) if i%2==0]    # we can also give coditions....
print(lst)                 