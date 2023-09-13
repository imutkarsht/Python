import os
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encode the given message

def encode(message,shift):
    for letter in message:
        position=alphabets.index(letter)
        new_position=position+shift
        if(new_position>25):
            new_position=new_position-26
        print(alphabets[new_position],end="")
        
# function to decode the given message
        
def decode(message,shift):
    for letter in message:
        position=alphabets.index(letter)
        new_position=position-shift
        if(new_position<0):
            new_position=new_position+26
        print(alphabets[new_position],end="")
                
# Driver Function of the code

def main():
    message=input("WELCOME TO CAESER CYPHER\nENTER THE MESSAGE\n").lower()
    shift=int(input("ENTER THE SHIFT NUMBER "))
    while True:
        ch=input("\ne to Encode\nd to Decode ").lower()
        match ch:
            case 'e':
                os.system('cls')
                print("\nThe encoded message is\n",)
                encode(message,shift)
                return
            case 'd':
                os.system('cls')
                print("\nThe decoded message is\n")
                decode(message,shift)
                return
            case _: 
                print("\nWrong choice enter again!")        
            
    

if __name__=="__main__":
    while True:
        main()
        cont=input("\nWant to try again?(y/n)").lower()
        if cont!='y':
            break
                   