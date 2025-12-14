def print_board(board):
    print()
    for row in board:
        for cell in row:
            print(cell, end=" | ")
        print()
    print()


def have_won(board, player):
    # check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # check columns
    for col in range(3):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True

    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


if __name__ == "__main__":
    board = [[" " for _ in range(3)] for _ in range(3)]

    player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"Player {player} enter row and column (0-2): ")

        try:
            row, col = map(int, input().split())
        except ValueError:
            print("Invalid input! Enter two numbers.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = player
        moves += 1

        if have_won(board, player):
            print_board(board)
            print(f"🎉 Player {player} has won!")
            break

        if moves == 9:
            print_board(board)
            print("Game is a draw")
            break

        player = "O" if player == "X" else "X"
