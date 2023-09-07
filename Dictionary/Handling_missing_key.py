# Handling missing Key value in a dictionary so that we could get a message instead of runtime error when key not found:
import collections
ex1={1:'a', 2:'b', 3:'c'}

# 1- Using key

if 4 in ex1:
    print(ex1[4])
else:
    print("Key not found: ")
    
# 2- using get()

print(ex1.get(1 , 'not found'))     # output --> a
print(ex1.get(5 , 'not found'))     # output --> not found

# 3- Using setdefault()

ex1.setdefault(4,'not found')
print(ex1[4])

# 4- Using defaultdict

deft=collections.defaultdict(lambda: 'key not found')

   # intitializing values 

deft[1]='a'
deft[2]='b'

print(deft[3])