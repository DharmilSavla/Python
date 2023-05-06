import time
import random
dictionary = open("words.txt").read().splitlines()

def typingtest():
    print("Welcome to the ultimate typing test")
    print("We are going to test your typing speed and accuracy")
    print("We are going to give you 3 words to type and time how fast you type them")
    print("This test works best on a high quality keyboard")
    
    times = []
    test = ""
    avg = 0
    chosen = ""
    word = ""
    valid = False
    correct = False
    
    print("Press Enter To Begin")
    start = input()
    while not correct:
        length = input("How Many Letters Do You Want The Words To Be: ")
        if length.isdigit():
            correct = True
            length = int(length)
        else:
            print("Please Enter An Integer")
    print()
    for i in range(0,3):
        while not valid:
            word = random.choice(dictionary)
            if len(word)==length and chosen!=word:
                valid = True
        print(word)
        startTime = time.time()
        while test != word:
            test = input()
            if test == word:
                endTime = time.time()
                speed = round((endTime-startTime),2)
                times.append(speed)
                print()
            else:
                print("Incorrect spelling")
        chosen = word
        valid = False
    print()
    
    for i in range(0,len(times)):
        print("Word",i+1,">",times[i],"seconds")
        avg = avg + times[i]
    
    print()
    
    print("Your average time was:", round(avg/3,2), "seconds")

typingtest()
                
            