x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
        
    case 4:
        print(" case is 4")
    case _:
        print(x)
    #default case is defined by case _. It is only matched when all above cases are not matched
    #unlike c/c++ break keyword is not required here             