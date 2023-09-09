# if control can't go inside for else will execute

for i in []:
    print(i)
else:
    print("Sorry! No i")
    
for j in range(6):
    print(j)
    if j==4 :
        break     
else:
    print("This will not get printed")       