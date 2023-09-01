num=int(input("Enter the number: "))
p=int(input("Enter The power upto which you want to raise the number: "))

pro=1
for i in range(0,p):
    pro=pro*num
    
print("The Value after Raising power is: ", pro)    