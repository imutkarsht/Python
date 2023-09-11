import random

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','%','^','&','(',')','_']

size=int(input("How long you want your password to be? "))
while True:
    alpha_no=int(input("How many alphabets? "))
    symbol_no=int(input("How many symbol? "))
    number_no=int(input("how many numbers?"))
    
    if(alpha_no+symbol_no+number_no!=size):
        print("Sum of all different characters must be equal to size... Enter again..")
        continue
    else:
        break
    

def generate_pass(alphabets,numbers,symbols,size,alpha_no,symbol_no,number_no):
    password=""
    for _ in range (0,alpha_no+1):
        password+=random.choice(alphabets)
    for _ in range (alpha_no,alpha_no+symbol_no):
        password+=random.choice(symbols)    
    for _ in range (alpha_no+symbol_no,alpha_no+symbol_no+number_no):
        password+=random.choice(numbers) 
    
    char_list = list(password)
    
    # Shuffle the list of characters
    random.shuffle(char_list)
    
    # Convert the shuffled list of characters back to a string
    shuffled_string = ''.join(char_list)
               
    return shuffled_string

print(generate_pass(alphabets,numbers,symbols,size,alpha_no,symbol_no,number_no))           