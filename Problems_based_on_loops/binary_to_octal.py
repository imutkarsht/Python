# Python program to convert a binary to octal

# Input binary number from user. Store it in a variable say binary.
binary=int(input("Enter the Binary number: "))

# Initialize a variable to store converted octal say octal = 0.

octal=''

# Find the last three digits of binary say digit = num % 1000.

while(binary!=0):
    digit=int(binary%1000)

# Find the octal equivalent (using binary to octal table) of the three binary digits found above.
    match digit:    
        case 000:
            octal+='0'        
        case 0o1:
            octal+='1'
        case 0o10:
            octal+='2'
        case 0o11:
            octal+='3'
        case 11:
            octal+='3'    
        case 100:
            octal+='4'
        case 101:
            octal+='5'
        case 110:
            octal+='6'
        case 111:
            octal+='7'
    binary=int(binary/1000)   

print(octal[::-1])    
         
# Add octal value of binary found in above step to octal, by increasing the place value.
# Remove the last three digits of the binary number. Since they are processed, say binary = binary / 1000.
# Increase the place value of octal by using place = place * 10.
# Repeat step 3 to 7 till binary > 0.