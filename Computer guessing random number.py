""" Author: Jacky Ho
    Date: November 10th, 2016
    Description: You think of a number between 1-100 and the computer guesses your number, while you tell him if it's higher or lower"""

import random

def main():
    """The computer attempts to guess the number that you guess and you tell it if its low, correct, or high"""
    while True:
        try:
            print "Hello! Think of a number between 1 and 100 and I will guess it! "
            guess = 50
            low=0
            high=100
            while True:
                try:
                    print "My guess is", guess
                    print "Am I?\n1. Too low\n2. Correct\n3. Too high"
                    ans = int(raw_input ("Which one? "))
                    ans = int(ans)
                    if ans != 1 and ans != 2 and ans != 3:
                        print "That is an invalid option."
                        continue
                    elif ans == 1:                   
                        if guess > low:
                            low = guess
                            if high - low == 1:
                                low = guess
                                guess = toolow(low,high)
                                print "The number you are thinking of must be", guess   
                            else:
                                toolow(low,high)
                                guess = toolow(low,high)
                    elif ans == 2:
                        print "Yay I win!"
                        break
                    elif ans == 3: 
                        if guess < high:
                            high = guess
                            if high - low == 1:
                                high = guess
                                guess = toohigh(low,high) 
                                print "The number you are thinking of must be", guess     
                            else:
                                toohigh(low,high)
                                guess = toohigh(low,high)  
                except ValueError:
                    print "That's not a number!"
                    continue                
        except ValueError:
            print "That's not a number!"
            continue
        break
def toolow(low,high):
    """The parameters are the lowest and highest values that you have indicated
       and the computer generates a new guess based on your requirements and returns
       the new guess as the return value"""
    newguess= random.randint (low+1,high-1)
    return newguess
def toohigh(low,high):
    """The parameters are the lowest and highest values that you have indicated
       and the computer generates a new guess based on your requirements and returns
       the new guess as the return value"""    
    newguess= random.randint (low+1,high-1)
    return newguess
main()


