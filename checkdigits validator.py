""" Author: Jacky Ho

    Date: November 23rd, 2016
    
    Description: This program uses a module to check whether
    a 12-digit UPC or 10-digit ISBN number is valid.
"""
import checkdigits
def main():
    while True:
        user = start()
        if user == "Quit":
            break
        if user == 1:
            ISBN()
        elif user == 2:
            UPC()
def start():
    while True:
        print "CHECK DIGIT VALIDATOR\n"
        print "What would you like to validate:\n"
        print "1. ISBN-10\n2. UPC-12\nQ. Quit Program\n"
        answer = raw_input ("What is your choice? ")
        if answer == "1":
            return 1
        elif answer == "2":
            return 2
        elif answer == "q" or answer == "Q":
            return "Quit"
        else:
            print "\nInvalid input, enter again.\n"
            continue        
def ISBN():
    code = input ("Enter the code without symbols: ")
    if checkdigits.is_ISBN10(code)==True:
        print "\nThis ISBN is valid!\n"
    else:
        print "\nThis ISBN is invalid!\n"
def UPC():
    code = input ("Enter the code without symbols: ")
    if checkdigits.is_UPC12(code)==True:
        print "\nThis UPC is valid!\n"
    else:
        print "\nThis UPC is invalid!\n"        
#calls function
main()