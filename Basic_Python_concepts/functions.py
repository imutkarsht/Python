# python program to demonstrate functions
# functions are mainly used to make a snippet of code reusable

def calc_gmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
    
a=9
b=8
c=8
d=7

#gmean=(a*b)/(a+b)
#print(gmean)


#gmean1=(c*d)/(c+d)
#print(gmean1)


# Instead of writting same code again and again we can simply call the function


calc_gmean(a,b)
calc_gmean(c,d)    
    