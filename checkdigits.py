""" Author: Jacky Ho

    Date: November 23rd, 2016
    
    Description: This module contains functions that perform calculations
    to check if 12-digit UPC and 10-digit ISBN codes are valid or not.
"""
def get_digit(number, position):
    #checks value of a digit in a number in a position
    return number/10**position % 10

def is_UPC12(number):
    odd_total = 0
    even_total = 0
    for position in range(1,13,2):
        #calls the get_digit function and adds it to the odd total
        odd_total += get_digit(number, position)
    for position in range(0,13,2):
        #calls the get_digit function and adds it to the even total
        even_total += get_digit(number, position)  
    #calcualtes step 4 of validating UPC
    total = (odd_total * 3) + even_total
    #determining if total from step 4 is equal to the check digit
    if 10 - (total % 10) == (total % 10):
        return True
    elif (total % 10) == 0 and (total % 10) == 0:
        return True
    else:
        return False
    
def is_ISBN10(number):
    weighted_value = 9
    total = 0
    for position in range(1,10):
        #calculates the digits multiplied by the weighted value
        total += get_digit(number,position)*weighted_value
        weighted_value -= 1
    #determines whether ISBN matches check digit
    if (total % 11) == (number % 10):
        return True
    else:
        return False