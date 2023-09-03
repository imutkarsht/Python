# Python Program to print 1's complement of a given binary

binary=str(input("Enter The binary Number: "))
for i in range(0, len(binary)):
    if(binary[i]=='1'):
        print("0", end="")
    else:
        print("1",end="")    