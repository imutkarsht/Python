# Split string method
import random
names_string=input("Give me names seperated by comma.")
names=names_string.split(",")  #It will create a list from all names above....
# i=len(names)
print("Printing a name randomly out of list....")
print(names)
# print(names[random.randint(0,i-1)])


# method 2

print(random.choice(names))