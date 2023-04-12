def asc():
    print("-----------------------------------------------")
    print("Please Enter An ASCII Value: ")
    ASC = input()
    decimal = ord(ASC)
    print("-----------------------------------------------")
    print("The Decimal equivalent is:", decimal)
    print("The Binary equivalent is: ", bin(decimal)[2:])
    print("The Hexadecimal equivalent is:", hex(decimal)[2:])
#----------------------------------------------------------------    
def hexa():
    print("-----------------------------------------------")
    print("Please Enter A Hexadecimal Value: ")
    Hexa = input()
    decimal = int(Hexa, base=16)
    print("-----------------------------------------------")
    print("The Decimal equivalent is:", decimal)
    print("The Binary equivalent is:" , bin(decimal)[2:])
    ASCII = chr(decimal)
    print("The ASCII equivalent is: ", chr(decimal))
#----------------------------------------------------------------    
def dec():
    print("-----------------------------------------------")
    validInput = False
    while not validInput:
        print("Please Enter A Decimal Value: ")
        Dec = input()
        if Dec.isnumeric():
            Dec = int(Dec)
            validInput = True
            ASCII = chr(Dec)
            print("-----------------------------------------------")
            print("The ASCII equivalent is: ", ASCII)
            Dec = int(Dec)
            print("The Binary equivalent is: ", bin(Dec)[2:])
            print("The Hexadecimal equivalent is:", hex(Dec)[2:])
        else:
            validInput = False
            print("Invalid input, please enter an integer")
#----------------------------------------------------------------
def bina():
    print("-----------------------------------------------")
    print("Please Enter A Binary Value: ")
    Bina = input()
    Dec = int(Bina, base=2)
    Bina = int(Bina)
    Asc = chr(Bina)
    Hexa = hex(Bina)
    print("-----------------------------------------------")
    print("The Decinal equivalent is: ", Dec)
    print("The ASCII equivalent is: ", Asc)
    print("The Hexadecimal equivalent is ", Hexa[2:])
#----------------------------------------------------------------    
def num_choice():
    print("-----------------------------------------------")
    print("Welcome to the ASCII, Hexadecimal, Decimal Converter")
    print("Press 1 if you are entering an ASCII value")
    print("Press 2 if you are entering a Hexadecimal value")
    print("Press 3 if you are entering a Decimal value")
    print("Press 4 if you are entering a Binary value")
    print("Press 5 if you are ending the session")
    choice = ""
    validInput = False
    while not validInput:
        choice = input("Please input a number: ")
        if choice== "1":
            ValidInput = True
            asc()
        elif choice == "2":
            ValidInput = True
            hexa()
        elif choice == "3":
            ValidInput = True
            dec()
        elif choice == "4":
            ValidInput = True
            bina()
        elif choice == "5":
            print("Session Ended")
            input()
        else:
            print("Invalid input, please enter a number between 1 and 5")
#----------------------------------------------------------------        
num_choice()
        
    
