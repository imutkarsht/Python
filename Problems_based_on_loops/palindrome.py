n=int(input("Enter a number: "))
num = n;
rev = 0
while n!=0 :
    dig = n % 10
    rev = rev *10 + dig
    n = int(n / 10)
    
if rev == num :
    print(f"{num} is a Palindrome number")
else :
    print(f"{num} is not a palindrome number")