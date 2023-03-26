import random
import time
from random_word import RandomWords
dictionary = RandomWords()

def typingtest():
    print("Welcome to the ultimate typing test")
    print("We are going to test your typing speed and accuracy")
    print("We are going to give you 3 words to type and time how fast you type them")
    print("This test works best on a high quality keyboard")
    
    times = []
    test = ""
    avg = 0
    chosen = ""
    
    print("Press any key to begin")
    start = input()
    for i in range(0,3):
        startTime = time.time()
        word = dictionary.get_random_word()
        while chosen == word:
            word = dictionary.get_random_word()
        print(word)
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
    print()
    
    for i in range(0,len(times)):
        print("Word",i+1,">",times[i],"seconds")
        avg = avg + times[i]
    
    print()
    
    print("Your average time was:", round(avg/3,2), "seconds")

typingtest()
                
            
