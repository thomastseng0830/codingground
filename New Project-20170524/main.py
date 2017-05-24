from random import randint

board = [[],[],[]]

for x in range(3):
    board[x].append("")
    board[x].append("")
    board[x].append("")



def print_board(board):
    for row in board:
        print row

print "Let's play Tic-Tac-Toe!"
print_board(board)

def has_winner(board):
    if board[0][0] == board[0][1] == board[0][2] == "X":
        return True
    return False

turn = 0
while turn < 10:
    row = int(raw_input("Row:"))
    col = int(raw_input("Col:"))
    if row < 4 and col < 4:
        board[row-1][col-1] = "X"
        print_board(board)
        turn += 1
    else:
        print "Please guess numbers between 1 and 3"
    if has_winner(board):
        print "GAME OVER"
        return
    
        

    
