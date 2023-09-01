#python program to swap first and last digit of a number

import math
# Logic to swap first and last digit of a number
# Begin:
#    read(num)

n=int(input("Enter the Number: "))
#     lastDigit ← num % 10;
last_digit=int(n%10)
#     digits ← log10(num);
digits=int(math.log10(n))
#     firstDigit ← num / pow(10, digits);
first_digit=int(n/math.pow(10,digits))
    
#     swappedNum ← lastDigit * pow(10, digits);
swapped_num=int(last_digit*math.pow(10,digits))
#     swappedNum ← swappedNum + num % pow(10, digits);
swapped_num=int(swapped_num+n % math.pow(10,digits))
#     swappedNum ← swappedNum - lastDigit;
swapped_num=int(swapped_num-last_digit)
#     swappedNum ← swappedNum + firstDigit;
swapped_num=int(swapped_num+first_digit)
# End

print("Number after Intechanging the digits is: ", swapped_num)