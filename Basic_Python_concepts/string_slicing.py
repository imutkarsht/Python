#program to demonstrate String Slicing and operations on the string

#syntax:    string_name[start:end:step]

names = "Utkarsh,Sachin"

# We can find length of string by using  len() function
print(len(names))

# we can slice a function using string_name[starting _index(inclusive) : ending Index(exclusive)]
# By default starting index is 0 and ending index is len(string_name)

print(names[0:7])            #This will print first 7 characters starting from names[0]

print(names[:5])             # it is equivalent to print(names[0:5])
print(names[: len(names)-3]) #it will print upto third last character starting from 0
                             #it is equivalent to print(names[: -3])
                             
print(names[-4:-2])          #output ---> ch ( c is at 10th place ie; len(names) ie; 14-4=10, also it will end at h instead of i as it is exclusive)

print(names[::2])            #this will skip every second character
print(names[-1:-14:-2])      #starting from end it will skip every second character  ie; nha,sat

print(names[::-1])           #it will print the given string in reverse