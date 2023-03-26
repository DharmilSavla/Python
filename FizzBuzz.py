def FizzBuzz():
    validNum = False
    while not validNum:
        print("Please Enter A Number Between 1-100")
        num = input()
        if num.isnumeric():
            num=int(num)
            validNum = True
        elif num == 'dog':
            print("Stop trying to break my code Mr Key")
        elif num == 'Top G' or num == 'top g':
            print("What colour is your bugatti?")
        else:
            print("Invalid input")
    
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0 and num%5 != 0:
        print("Fizz")
    elif num%3 != 0 and num%5 == 0:
        print("Buzz")
    else:
        print(num)

FizzBuzz()