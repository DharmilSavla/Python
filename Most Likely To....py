import random

def mostLikely():
    people = ["Dharmil", "Jenny", "Yoel", "Jarad", "Noel", "Natasha", "Kseniia","Juan","Maksim"]

    print("Most likely to...")
    event = input()
    person = random.choice(people)
    print(person)
    print()
    menu()

def end():
    print("Thank you for playing")

def menu():
    print("Welcome to Most Likely To")
    print("Press 1 if you want to play")
    print("Press 2 if you want to quit")
    check = False
    while not check:
        selection = input()
        if selection.isnumeric():
            selection = int(selection)
            if selection == 1:
                check = True
                mostLikely()
            elif selection == 2:
                check = True
                end()
            else:
                print("Please enter 1 or 2")
                check = False
        else:
            print("Please enter a number")

menu()

