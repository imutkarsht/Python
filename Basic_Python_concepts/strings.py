#Python program to demostrate strings 

#In Python we can initialise strings either by "" or ''

name = "Utkarsh"
surname = "Tiwari"
friend = 'Sachin'


print("hello, "+ name) #This will concatenate hello with the string in variable name


# we use '''...''' or """...""" to Initialise multiline strings

multi= '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident,sunt in culpa
qui officia deserunt mollit anim id est laborum.'''

print(multi)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

#print(name[7]) ---> This will throw an error