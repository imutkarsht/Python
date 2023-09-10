# A simple Encoder Decoder Program in Python that encodes a message in following way
# If length of message is less or equal to three, it simply returns that word in reverse
# if length of message is more than 3, It appends first letter to the end and generate three random letters in the beginning

import string
import random
import os

def code(msg):
    if len(msg)<=3 :
        return msg[::-1]
    else:
        # Generate three random characters
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        
        # Append the first letter of the name to the end
        encoded_name = random_chars + msg[1:] + msg[0]
        return encoded_name
    
def decode(msg):
    if len(msg)<=3:
        return msg[::-1]
    else:
        first_letter=msg[-1]
        decoded_name=first_letter+msg[3:-1]
        return decoded_name
 
print("\t\t\t\tENCODER DECODER\n") 
while(True):
           
    choice=int(input("Enter your choice\n1. for encoding\n2. for decoding\n"))
    os.system('cls')
    if(choice==1 or choice==2):
        match choice:
            case 1:
                message=input("Enter the message you want to Encode.... ")
                print(f"The Encoded message is {code(message)}")
            case 2:
                message=input("enter the messsage you want to Decode... ")
                print(f"The Decoded message is {decode(message)}")    
        break
    else:
        print("Invalid Input! please Enter either 1 or 2")    
