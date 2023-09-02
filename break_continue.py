# break   --> used to exit loop at particular iteration
#continue --> used to skip loop at a particular iteration

for i in range(12):
    if(i==10):
        break                      #It will end loop when this is encountered
    print("4 X", i+1,"=",4*(i+1))
    
    
    
for i in range(12):
    if(i==10):
        continue                     #It will skip iteration when this is encountered
    print("4 X", i+1,"=",4*(i+1))
