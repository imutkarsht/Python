# Python program to demonstrate while loop
i=0
while (i<3):
    print(i)
    i=i+1
    
# it is similar to 
# for i in range(3):
#     print(i) 
 
#this code will allow user to input a number and print it unless entered input is less or equal to 20    
i= int(input("Enter the number: "))
while(i<=20):
    i=int(input("Enter the number: "))
    print(i)    
# we can also use else with while loop
else:
    print("loop over")
        

# count = 5
# while(count>0):
#     print("This is an infinite loop:")
#     count=count+1    

# Decreamenting while loop

count=5
while(count>0):
    print(count)
    count=count-1