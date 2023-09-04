#python code to print all permutations of [i,j,k] such that it doesn't add up to n ie; i+j+k!=n

x = int(input("Enter the value of i: "))
y = int(input("enter the value of j: "))
z = int(input("enter the value of k: "))
n = int(input("enter the value of n: "))

l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k)!=n]

print("All possible permutaions of [i,j,k] such that i+j+k!=n are: ")

print(l)