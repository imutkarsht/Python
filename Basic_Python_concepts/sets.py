# Python program to demonstrate sets in python....

s={2,4,2,6}
print(s)      # output---> {2,4,6}  Repeated elements are counted only once

# Elements occur in random and doesn't mainntain their order....

utkarsh={}
print(type(utkarsh))        #output will be <'class dict'> as it will create empty set

utkarsh=set()  #that is correct way to create an empty set
print(type(utkarsh))        