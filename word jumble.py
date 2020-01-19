"""Author: Jacky Ho
   Date : December 16,2016
   Description: Takes a word and scrambles it to create a new word.
"""
import random
word= raw_input ("Please enter your word: ")

def word_jumble(word):
    new_word= ""
    for letter in word:
        new_letter= random.randrange(len(word))
        new_word = new_word+word[new_letter]
        word = word[:new_letter]+ word[new_letter+1:]
    return new_word

print word_jumble(word)
