# Return the count of a given substring from a string

string=input("Enter the String....")
sub_string=input("Enter the Substring you want to check.....")

count=0

for i in range(len(string)-1):
    count+=string[i:i+len(sub_string)]==sub_string
    
print("The Substring ",sub_string," apeeared ",count," times")    