# methods in python to manipulate list..

l=[3,1,1,4,2,5,6]
print(l)

l.append(7)                 # will add 7 at end of list
print(l)

l.sort()                    #it will sort list in ascending order
print(l)

l.sort(reverse=True)        # will sort list in descending order
print(l)

l.reverse()                 # will reverse order of elements 
print(l)

print(l.index(1))           # will print first index of list
print(l.count(1))           # will print how many times 1 has appeared in list

l.insert(1,99)              # will insert 99 on index 1
print(l)

m=[10,11,12]

l.extend(m)                 # will add elements of m at end of l
print(l)