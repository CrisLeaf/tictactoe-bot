from minimax import (
    check_win, check_draw, is_valid_position, get_next_move
)

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def print_board():
    for row in board:
        print(row)

def drop_piece(board, i, j, piece):
    board[i][j] = piece
    return board

def player_move():
    u = input("X Position:")
    i, j = int(u[0]), int(u[1])

    if is_valid_position(board, i, j):
        drop_piece(board, i, j, 1)
        print_board()
        print("\n")
    else:
        print("Invalid Position")
        player_move()

def bot_move():
    move = get_next_move(board, -1)
    drop_piece(board, int(move[0]), int(move[1]), -1)
    print_board()


if __name__ == "__main__":
    while True:
        player_move()
        if check_win(board, 1):
            print("Player wins !!")
            break

        elif check_draw(board):
            print("Draw !!")
            break

        bot_move()
        if check_win(board, -1):
            print("Bot wins !!")
            break
