# Calculate income tax for the given income by adhering to the rules below
# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000


amount=int(input("Enter the amount: "))

if(amount<=10000):
    print("The total amount of tax you need to pay is: 0 INR")
elif(amount>10000 and amount<=20000):
    tax=(amount-10000)/10
    print("The total amount of tax you need to pay is: ",tax, "INR")
elif(amount>20000):    
    tax=((amount-20000)/5)+1000
    print("The total amount of tax you need to pay is: ",tax, "INR")