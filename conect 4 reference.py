"""
import random

def who_goes_first():
    while True:
#change variable
        go = raw_input("Do you want to go first? (Y or N): ")
        if go == "y" or go =="Y":
            return True
        elif go == "n" or go == "N":
            return False
        else:
            print "Please enter a valid answer."

def game_board(board):
    print "",
    for column in range(len(board[0])): 
        print "", column, "",
    print
    for row in range(len(board)):
        #https://www.tutorialspoint.com/python/string_join.htm
        print "|" + "", " | ".join(board[row]) + " |"  
def player_x(board):   
    while True:
        try:
            column = input("Please enter a column: ")
            if column >= 0:
                row = int(moveCheck(board, column, True))
                break
            else:
                print "Please enter a valid column."
        except:
            print "Please enter a valid column."
    return row, column
def computer_o(board):
    while True:
        try:
            column = random.randrange(len(board[0]))
            row = moveCheck(board, column, False)
            break
        except:
            pass
    return row, column
def turn_check(board, column, player):
    for row in range(len(board)-1, -1, -1):
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
def winner_check(board, row, col, playerTurn):

    result = 3
    
    for index in range(len(board)):
        for index_2 in range(len(board[index])):
            if board[index][index_2] == " ":
                result = 0
                break
            
    for index in range(4):
        rowPossible = False
        columnPossible = False
        if row-index>=0 and row-index+3<len(board):
            rowPossible = True
            if board[row-index][col]==board[row-index+1][col]==\
               board[row-index+2][col]==board[row-index+3][col]:
                if playerTurn:
                    result = 1
                else:
                    result = 2     
        if col-index>=0 and col-index+3<len(board[0]):
            columnPossible = True
            if board[row][col-index]==board[row][col-index+1]==\
               board[row][col-index+2]==board[row][col-index+3]:
                if playerTurn:
                    result = 1
                else:
                    result = 2
        if rowPossible and columnPossible:
            if board[row-index][col-index]==board[row-index+1][col-index+1]==\
               board[row-index+2][col-index+2]==board[row-index+3][col-index+3]:
                if playerTurn:
                    result = 1
                else:
                    result = 2
        if rowPossible and col+index-3>=0 and col+index<len(board[0]):
            if board[row-index][col+index]==board[row-index+1][col+index-1]==\
               board[row-index+2][col+index-2]==board[row-index+3][col+index-3]:
                if playerTurn:
                    result = 1
                else:
                    result = 2
    return result

def hof():
    try:
        fame = open("HallOfFame.txt", "r")
        print "THE HALL OF FAME"
        for name in fame:
            number=1
            print str(count) + ".", name
            print
            number += 1    
    except IOError:
        print "No Human Has Ever Beat Me.. mwah-ha-ha-ha!"
        
def hof_entry(name):
    fame = open("HallOfFame.txt", "a")
    fame.write(name+"\n")
    fame.close()
def board_size(board):
    while True:
        try:
            rows =input("Enter the amount of rows (5-7 rows): ")
            if rows >= 5 and rows <= 7:
                break
            else:
                print "Please enter a valid amount of rows."
        except:
            print "Please enter a valid amount of rows."
    while True:
        try:
            columns =input("Enter the amount of colums (6-8 columns): ")
            if columns >= 6 and columns <= 8:
                break
            else:
                print "Please enter a valid amount of columns."
        except:
            print "Please enter a valid amount of columns."
    for row in range(rows):
        board.append([])
        for column in range(columns):
            board[row].append(' ')
def main(): 
    result = 0
    board = []
    
    playerTurn = first()
    print
    
    while result == 0:
        if playerTurn:
            print "This is your current board:"
            showGame(board)
            row, column = playerMove(board)
            result = check(board, row, column, playerTurn)
            playerTurn = False
        else:
            row, column = computerMove(board)
            result = check(board, row, column, playerTurn)
            playerTurn = True
    print "This is your final board:"
    showGame(board)
    if result == 1:
        print "Congratulations, you won!"
    elif result == 2:
        print "The computer won! Better luck next time!"
    elif result == 3:
        print "There is a stalemate!"
"""    