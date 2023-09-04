# python program to demonstrate tuple
tup=(1,2,3,4,5)

# tuples are unchangable

# tup[0]=90 ---> This will throw an error

country=("India","Pakistan","Australia","Newzealand","England","SouthAfrica","Netherlands","Afghanistan","Srilanka","Bangladesh")

# checking of item in tuples

if "India" in country:
    print(True)

# Tuple can be sliced too

tup2= tup[1:3]
print(tup2)

# Tuple Methods...
# to change a tuple you have to change it to a list and then change the list and covert back list to tuple

temp=list(country)
temp.append("Russia")
temp.pop(3)
country=tuple(temp)     
print(country)

# We can concatenate two tuples to make a Third Tuple..