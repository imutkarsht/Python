s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))     # union 
print(s1,s2)            # value of s1 and s2 will remain unchanged

# we have to use update method toupfate set s1

s1.update(s2)
print(s1,s2)

cities={'delhi','oslo','madrid','rome'}
cities2={'delhi','newyork','madrid','paris'}

print(cities.intersection(cities2))    # Intersection
cities.intersection_update(cities2)
print(cities,cities2)

# isdisjoint()    --> If item of one set is given in other set
# pop()           --> will delete a random value in set
# clear()         --> will delete all values
# del             --> will delete entire set