import random


def main():
    word_bank= ["hello", "goodbye","farewell","greetings"]
    
    for number in range(4):
        word_index= random.randrange(len(word_bank))
        word= word_bank[word_index]
        word_jumble(word_bank,word_index,word)
    
    
    
def word_jumble(word_bank,word_index,word):
    new_word=""
    original_word= word
    for letter in word:
        new_letter= random.randrange(len(word))
        new_word = new_word+word[new_letter]
        word = word[:new_letter]+ word[new_letter+1:]
    print new_word
    while True:
        guess = raw_input ("Guess the word from hello, goodbye, farewell, greetings: ")
        if guess == original_word:
            del word_bank[word_index]
            print "correct"
            break
        else:
            continue

        
main()