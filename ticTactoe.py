print("welcome to my Tic Tac Toe Game")
'''
Tic-Tac-Toe: A Solution
Author: Bro. Manley
Improved by Mohamed Nasiru
'''

#creating a board with 9 grids
def createBoard():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board
#display the board to users
def drawBoard(board):
    print()
    print(f"{board[0]}| {board[1]}|{board[2]}")
    print('---------')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('---------')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
#determining whether is a draw
def gameDraw(board):
    for box in range(9):
        if board[box] != "x" and board[box] != "o":
            return False
    return True 

def gameWin(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# this handles player moves and make sure a player enter a valid number
def playerMove(player, board):
    
    while True:
        try:
            move= int(input(f"{player}' please choose a box (1-9): "))
            if move > 0:
                break 
        except IndexError:
                print("Enter a value index")
        except ValueError:
                print("enter a value number")
            
        board[move - 1] = player



def nextPlayer(current):
    
    
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


#main function do all the function call
def main():
    player = nextPlayer("")
    board = createBoard()
    while not (gameDraw(board) or gameWin(board)):
        drawBoard(board)
        playerMove(player, board)

        player = nextPlayer(player)
    drawBoard(board)
    print("Good game. Thanks for playing!") 

if __name__ == "__main__":
    main()
