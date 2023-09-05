#python program to demonstrate f-string 
#traditional way......

letter= " My name is {} and  i'm from {}"
country="India"
name= "Utkarsh"

print(letter.format(name,country))

# using f-string.....

print(f"Hey my name is {name} and I'm from {country}: ")

price=49.0222445

txt=f"for only {price: .2f} INR!"
print(txt)