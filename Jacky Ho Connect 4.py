"""
Author: Jacky Ho
Date: Jan 25,2017
Description: Game of connect four that is played against the coputer. User is
able to decide the size of the board as well as whether to go first or not. Win 
and put your name into the hall of fame."""
import random

def main(): 
    """Mainline logic of program"""
    
    board = []
    state = 0
    
    hof() # calls function to print the hall of fame
    print""
    board_size(board) #calls functions and prompts the user for the size of board they would like
    print""
    player_turn = who_goes_first()#Calls function to allow user to decide to go first or not
    print""
    
    while state == 0: # keeps the loop running until someone connects 4 or stalemates
        if player_turn:
            print "Here is the board, take your turn: "
            game_board(board) # prints the game board
            row, column = player_x(board) 
            state = winner_check(board, row, column, player_turn)
            player_turn = False # swaps turn over to computer
        else:
            row, column = computer_o(board)
            state = winner_check(board, row, column, player_turn)
            player_turn = True #swaps turn over to player
    print "Here is the ending board: "
    game_board(board) # displays the final board
    if state == 1:
        print "There is a stalemate!" #incase of tie
    elif state == 2:
        print "Congratulations, you won!" #incase of player win
        name=raw_input("Enter your name for the hall of fame: ")
        hof_entry(name) #user is prompted to enter name for the hall of fame
    elif state == 3:
        print "The computer won! Better luck next time!" #incase of computer win
        
def who_goes_first():
    """Asks user whether or not they want to go first"""
    while True:
        go = raw_input("Do you want to go first? (Y or N): ")#user input for y/n
        if go == "y" or go =="Y":
            return True
        elif go == "n" or go == "N":
            return False
        else: #incase if the answer yes or no is not given
            print "Please enter a valid answer."
            
def game_board(board):
    """Takes List created in board size function and converts it into connect 4
    like board"""
    print "",
    for column in range(len(board[0])):
        print "", column, "", # numbers the connect 4 columns
    print
    for row in range(len(board)):
        #https://www.tutorialspoint.com/python/string_join.htm
        print "|" + "", " | ".join(board[row]) + " |" #creates the columns on board
        print "|"+"---+" * int(column)+"---|"
        
def player_x(board):   
    """Promtps the user for the column that they would like to play into next"""
    while True:
        try:
            column = input("Please enter a column: ") #user input for move
            if column >= 0:
                row = turn_check(board, column, True)
                break
            else: #incase of invalid input
                print "Please enter a valid column."
        except: #incase of invalid input
            print "Please enter a valid column."
    return row, column

def computer_o(board):
    """Takes a random number and converts it into an integer that is played as 
    the computers choice of column for that turn"""
    while True:
        try:
            column = random.randrange(len(board[0])) # picks random column for computer
            row = turn_check(board, column, False)
            break
        except:
            pass
    return row, column

def turn_check(board, column, player):
    """checks if the move made is valid then assigns either x or o depending on 
    if it is computer or players turn into column in the list"""
    for row in range(len(board)-1, -1,-1):
        try:
            if board[row][column] == " ":
                if player:
                    board[row][column] = "X"
                    inputRow = row
                    break
                else:
                    board[row][column] = "O"
                    inputRow = row
                    break
        except:
            return inputRow
    return inputRow

def winner_check(board, row, column, player_turn):
    """Analyses the board to return a value regarding the state of the game 
    representing either a win, loss, tie or continuation of play"""
    state = 1  #1 Representing stalemate
    for index in range(len(board)):
        for index_2 in range(len(board[index])):
            if board[index][index_2] == " ":
                state = 0 #Empty spaces in the board are searched for
                break
    for index in range(4):
        rowPossible = False
        columnPossible = False
        # Checks for horizontal connect 4
        if row-index>=0 and row-index+3<len(board):
            rowPossible = True
            if board[row-index][column]==board[row-index+1][column]==\
               board[row-index+2][column]==board[row-index+3][column]:
                if player_turn:
                    state = 2
                else:
                    state = 3   
        # Checks for vertical connect 4
        if column-index>=0 and column-index+3<len(board[0]):
            columnPossible = True
            if board[row][column-index]==board[row][column-index+1]==\
               board[row][column-index+2]==board[row][column-index+3]:
                if player_turn:
                    state = 2
                else:
                    state = 3
        # Checks for diagonal connect 4
        if rowPossible and columnPossible:
            if board[row-index][column-index]==board[row-index+1][column-index+1]==\
               board[row-index+2][column-index+2]==board[row-index+3][column-index+3]:
                if player_turn:
                    state = 2
                else:
                    state = 3
        # Checks for diagonal connect 4
        if rowPossible and column+index-3>=0 and column+index<len(board[0]):
            if board[row-index][column+index]==board[row-index+1][column+index-1]==\
               board[row-index+2][column+index-2]==board[row-index+3][column+index-3]:
                if player_turn:
                    state = 2
                else:
                    state = 3
    return state

def hof():
    """opens the hall of fame text file and reads it or taunts the user if 
    file does not exist"""
    try:
        fame = open("HallOfFame.txt", "r")
        print "THE HALL OF FAME" # opens hall of fame file and prints out names
        number = 1
        for name in fame:
            print str(number) + ".", name
            print ""
            number += 1
    except IOError:
        print "No Human Has Ever Beat Me.. mwah-ha-ha-ha!"
        
def hof_entry(name):
    """takes a name and adds it into the hall of fame text file"""
    fame = open("HallOfFame.txt", "a")
    fame.write(name+"\n")
    fame.close()
    
def board_size(board):
    """Asks the user for input of the size of board they would like to play on
    and translates that into a bunch of sublists within a list"""
    while True:
        try:
            rows =input("Enter the amount of rows (5-7 rows): ")
            if rows >= 5 and rows <= 7: #asks user for number of rows
                break
            else: #incase of invalid input
                print "Please enter a valid amount of rows."
        except:
            print "Please enter a valid amount of rows."
    while True:
        try: # Asks user for number of columns
            columns =input("Enter the amount of colums (6-8 columns): ")
            if columns >= 6 and columns <= 8:
                break
            else:# incase of invalid input
                print "Please enter a valid amount of columns."
        except:
            print "Please enter a valid amount of columns."
    for row in range(rows):
        board.append([]) #converts the number of rows and columns requested into 
        for column in range(columns): #list containing sublists
            board[row].append(' ')
main()