# Print the sum of the current number and the previous number

n = int(input("Enter The Range: "))
for i in range(0,n):
    previous_num=i
    current_num=i+1
    print("current number ",current_num,"\tprevious number ",previous_num,"\tsum: ",current_num+previous_num)
    