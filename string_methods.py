#Pyhton program to demonstrate use of string methods
name= "!!UtKarSh!!UtKarSh!!!"

#Strings are Immutable

print("Length of the string is ", len(name))     #len() will give length of string
print("The string in upper case ", name.upper()) #upper() converts string to upper case
print("The string in upper case ", name.lower()) #lower() converts string to lower case
print(name.rstrip("!"))                          #it removes all trailing characters
# output ---> !!Utkarsh

print(name.replace("UtKarSh","Rohit")) #replaces all occurances of a string with given string
# output ---> !!Rohit!!Rohit!!!

#capitalise()  ---> converts first character to capital and other to lower case( if not already)

print(name.count("!"))     #count() ---> gives number of occurances of a charcter in string

#endswith() ---> checks if a string ends with a specific character

#find()    ---> gives first occurance of a specific string
#index()   ---> same as find but raises an exception if not found
#isalnum() ---> checks if string is alphanumeric( a-z, A-Z, 0-9)
#isalpha() ---> checks if string only have characters( A-Z or a-z)
#islower() ---> checks if all characters are in lower case
#isupper() ---> checks if all characters are in upper case
#isprintable() ---> Returns true only when string doesn't have escape characters
#istitle()  ---> checks if first letter of each word in string is capital
#swapcase() ---> converts upper case to lower and lower to upper

name1= "SinCHan"
print(name1.swapcase())