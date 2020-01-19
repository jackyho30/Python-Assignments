

import random
def main():
  
   total = 0
   ran = random.randint (1,1000)
   print ran
   print "I have a number between 1 and 1000.\nCan you guess my number?"
   while True:
      
      try:
         
         num = int(raw_input("Please type your guess: "))
         num = int(num)
         if num > 1000 or num < 0:
            print "That number isn't even between 1 and 1000!"
            continue
         elif num == ran:
            print "Excellent! You guessed the number!"
            total += 1
            break
         elif num > ran:
               print "Too high. Try again!"
               total += 1
         elif num < ran :
            print "Too low. Try again!"
            total += 1
            if num == ran:
               
               ans = raw_input ("Would you like to play again (y or n)?")
               if ans == "y":
                  print "New number!"
                  total = 0
                  ran = random.randint (1,1000)
                  if ans == "n":
                     print "Thank you! Bye!"
                     break
                  if total == 10:
                     print "TEN TRIES AND YOU STILL DIDN'T GET IT? YOU SUCK!"
                     print "The number I was thinking of was", ran
                     break
      except ValueError:
         print "That's not a number! "
         continue
main()
