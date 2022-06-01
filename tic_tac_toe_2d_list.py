SIZE = 3
def make_board():
    return [[" "  for _ in range(SIZE)] for _ in range(SIZE)]

def print_board(board):
    for row in board:
        print(row)

def make_move(board, symbol):
    no_move = True
    while no_move:
        try:
            move = input("Enter a move (row, col): ")
            tokens = move.split()
            row = int(tokens[0])
            col = int(tokens[1])
            if board[row][col] == " ":
                board[row][col] = symbol
                no_move = False
            else:
                print("Invalid move, Please try again")
        except IndexError:
            print("Invalid move, Please try again")
    print_board(board)

def main():
    board = make_board()
    print_board(board)
    symbol = "X"
    for _ in range(SIZE * SIZE):
        make_move(board, symbol)
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
    print("Game Over!")

if __name__ == '__main__':
    main()