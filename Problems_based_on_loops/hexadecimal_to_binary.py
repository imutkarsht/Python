# Python Program to convert Hexadecimal to binary

hexa=str(input("Enter the value in hexadecimal: "))
binary=''
for i in range(len(hexa)):
    match hexa[i]:
        case '0':
            binary+='0000'
        case '1':
            binary+='0001'
        case '2':
            binary+='0010'
        case '3':
            binary+='0011'
        case '4':
            binary+='0100'
        case '5':
            binary+='0101'
        case '6':
            binary+='0110'
        case '7':
            binary+='0111'
        case '8':
            binary+='1000'
        case '9':
            binary+='1001'
        case 'A':
            binary+='1010'
        case 'B':
            binary+='1011'
        case 'C':
            binary+='1100'
        case 'D':
            binary+='1101'
        case 'E':
            binary+='1110'
        case 'F':
            binary+='1111'
            
print("The Equivalent binary is\n", binary)            