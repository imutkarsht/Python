# Python Program that take name of bidders and their bid until they want and shows maximum bid in end when all bids are done

from os import system
Bidders={}  
def get_input(Bidders,i):
    name=input("Enter Your Name ")
    bid=int(input("Enter the Bid amount "))
    Bidders[name]=bid

def check_max(Bidders):
    max_ammount=0
    for key in Bidders:
        if Bidders[key]>max_ammount:
            max_ammount=Bidders[key]
            max_bidder=key
    print(f"The maximum bid was made by {max_bidder} of Ammount INR {max_ammount}")       
             
       
def main():
    i=0
    print("Welcome to the blind auction\n")
    while True:
        get_input(Bidders,i)
        system('cls')
        i=i+1
        ch=input("Want to Enter again?(y/n) ")
        if(ch!='y'):
           break
    check_max(Bidders)
    
if __name__=="__main__":
    main()    