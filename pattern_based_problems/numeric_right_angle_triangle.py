# Print the following pattern
#      1 
#      2 2 
#      3 3 3 
#      4 4 4 4 
#      5 5 5 5 5

rows=int(input("Enter the Number of rows: "))

for i in range(rows):
    for j in range(i):
        print(i,end="")
    print("")    