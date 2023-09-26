ch = input("Would You Like to Play the game(y/n)\t").lower()
        system("cls")
        if ch == "n":
          system('cls')
          print("Bye Have a nice day...")
          break
        elif ch=='y':
          main()
        else:
          print("Please Enter A valid response...")