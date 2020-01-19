def main():
    """Our Main Game Loop:"""
     
    free_cells = 9
    users_turn = True
    ttt_board = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] ]
 
    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1
         
    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print "Y O U   W O N !"
    elif (winner(ttt_board) == 'O'):
        print "I   W O N !"
    else:
        print "S T A L E M A T E !"
    print "\n*** GAME OVER ***\n"
  
  
def display_board(board):
    print "   0   1   2"
    print "0: " + board[0][0]+" | "+board[0][1]+" | " + board[0][2]
    print "  ---+---+---"
    print "1: " + board[1][0]+" | "+board[1][1]+" | " + board[1][2]
    print "  ---+---+---"
    print "2: " + board[2][0]+" | "+board[2][1]+" | " + board[2][2]
    print
def winner(board):
    # Check rows for winner
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and\
           (board[row][0] != " "):
            return board[row][0]
 
    # Check columns for winner
 
     
    # Check diagonal (top-left to bottom-right) for winner
 
     
    # Check diagonal (bottom-left to top-right) for winner
 
     
    # No winner: return the empty string
    return ""

def make_user_move(board):
    valid_move = False
    while not valid_move:
        row = input("What row would you like to move to (0-2):")
        col = input("What col would you like to move to (0-2):")
        if (0<=row<=2) and (0<=col<=2) and (board[row][col] == " "):
            board[row][col] = 'X'
            valid_move = True
        else:
            print "Sorry, invalid square. Please try again!\n"
# Start the game!
main()