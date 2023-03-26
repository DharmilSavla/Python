import turtle
t = turtle.Turtle()
g = turtle.getscreen()
from random_word import RandomWords
dictionary = RandomWords()

def hangman(count):
    t.speed(700)
    t.pensize(5)
    if count == 1:
        t.backward(100)
        t.forward(200)
    if count == 2:
        t.backward(100)
        t.left(90)
        t.forward(300)
    if count == 3:
        t.right(90)
        t.forward(150)
    if count == 4:
        t.right(90)
        t.forward(25)
    if count == 5:
        t.right(90)
        t.circle(30, 540)
    if count == 6:
        t.right(90)
        t.forward(100)
    if count == 7:
        t.right(45)
        t.forward(60)
        t.backward(60)
        t.left(45)
    if count == 8:
        t.left(45)
        t.forward(60)
        t.backward(60)
        t.right(45)
        t.right(180)
    if count == 9:
        t.forward(65)
        t.left(45)
        t.forward(60)
        t.backward(60)
        t.right(45)
    if count == 10:
        t.right(45)
        t.forward(60)
        t.backward(60)
        t.left(45)
        t.penup()
        t.goto(0,0)
        g.bgcolor('red')
        

guess = dictionary.get_random_word()
split = list(guess)
userWord = "_"*len(split)
userWord = list(userWord)
word = (' '.join(userWord))
print(word)

print()

print("Welcome to Python Hangman")
print("Python will generate a random word")
print("You need to guess letters and we will check if they are in the word")
print("You will only get 10 wrong guesses")
print("Please only enter lowercase letters")
print("-------------------------------------------------")

guessed = False
inWord = False
new_lst = ""
letters = []
entered = ""
count = 0

while not guessed:
    check = False
    if count == 10:
        guessed = True
        print("Sorry, you've run out of guesses")
        print("The word was", guess)
        check = True
    if userWord==split:
        guessed = True
        print("Well done, you guessed the word")
        print("The word was", guess)
        g.bgcolor('light green')
        check = True
    while not check:
        inWord = 0
        user = input("Please enter a lowercase letter or word: ")
        print()
        if user.isalpha():
            check = True
            if len(user)>1:
                if user == guess:
                    guessed = True
                    inWord = 2
                if user != guess:
                    inWord = 3
            else:    
                for i in range(0,len(guess)):
                    if user==guess[i]:
                        userWord[i] = split[i]
                        new_lst=(' '.join(userWord))
                        inWord = 1
            if inWord == 3:
                print("Sorry, that is not the word")
                letters.append(user)
                count += 1
                hangman(count)
            if inWord==2:
                print("Well done, you guessed the word")
                print("The word was", guess)
                g.bgcolor('light green')
            if inWord==1:
                print("Yes, that letter is in the word")
                print(new_lst)
            if inWord ==0:
                letters.append(user)
                entered = ",".join(letters)
                print("Nope, that letter is not in the word")
                count+=1
                print(new_lst)
                hangman(count)
            print()
            print("These are the letters you guessed:", entered)
        else:
            check = False


    




    
    