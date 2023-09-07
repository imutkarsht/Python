dic = {
    "utkarsh": "human",
    "spoon" : "object"
}

print(dic)
print(dic["utkarsh"])

#Dictionary is used to create a mapping

info ={
    312:'utkarsh',
    342:'Sachin',
    356: 'abhay'
}

print(info[312])  # It will give error when key not found
print(info.get(112))  # it will return none when key not found

# iterating to print all values
for key in info.keys():
    print(f"The value corresponding to the key {key} is: ",info[key])    
    
ep1={122:65, 123:89, 567:69, 670:69}
ep2={222:67, 566:90}

ep1.update(ep2)    # will add all keys of ep2 in ep1
print(ep1)

# ep1.clear()    ---> will delete all elements in dictionary
# ep1.pop(item)  ---> will clear item from dic ep1    