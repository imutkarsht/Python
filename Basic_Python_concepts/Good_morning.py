# A python program that greet users according to time of the day

import time

timestamp= time.strftime("%H:%M:%S")
print(timestamp)

a=int(time.strftime("%H"))

if(a>4 and a<12):
    print("Good Morning! Sir")
elif(a>=12 and a<17):
    print("Good Afternoon!,Sir") 
elif(a>=17 and a<22):
    print("Good morning! Sir")      
else:
    print("Good Night! Sir")    