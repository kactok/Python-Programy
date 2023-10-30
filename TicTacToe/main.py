# Tic Tac Toe game for 2 players

# O always has a first turn
current_turn = 'O'


def display_board(values: []) -> str:
    """Display the game board"""
    board = f"{values[0]} | {values[1]} | {values[2]}\n" \
            f"{values[3]} | {values[4]} | {values[5]}\n" \
            f"{values[6]} | {values[7]} | {values[8]}"
    return board


def check_win(board: [], turn: str) -> str:
    """Check if win/draw"""
    step = 1
    x = 3
    add_end = 3
    # check columns and rows
    for _ in range(2):
        start = 0
        stop = x
        for _ in range(3):
            count = 0
            for row_col in board[start:stop:step]:
                if row_col == turn:
                    count += 1
                if count == 3:
                    return "win"
            start += add_end
            stop += add_end
        step += 2
        x += 7
        add_end = 1

    # check diagonal
    if board[0] == board[4] == board[8] == turn:
        return "win"
    if board[2] == board[4] == board[6] == turn:
        return "win"
    if board.count("-") == 0:
        return "draw"


def change_player() -> str:
    """Change of turn"""
    global current_turn
    if current_turn == 'X':
        current_turn = 'O'
    else:
        current_turn = 'X'
    return current_turn


def free_field(board: [], players_choice: int) -> [bool]:
    """Check if field is already occupied"""
    if board[players_choice - 1] == 'O' or board[players_choice - 1] == 'X':
        return False
    return True


def main():
    cont = True
    while cont:
        if_winner = False
        board = ["-" for field in range(1, 10)]

        # display example board with numbers as a fields
        example_board = [field for field in range(1, 10)]
        print(f"TIC TAC TOE\n{display_board(example_board)}\n")

        # Game is on until there is a winner/draw
        while not if_winner:
            try:
                players_choice = int(input(f"{current_turn} turn. Select a flied (1-9): "))
                # Check if field is free
                if free_field(board, players_choice):
                    # Change value to X/O
                    board[players_choice - 1] = current_turn
                    # display updated board
                    print(display_board(board))
                else:
                    print("The field is already occupied!")
                    continue
            except ValueError:
                print("That's not a valid field!")
            else:
                if check_win(board=board, turn=current_turn) == 'win':
                    print(f"{current_turn} is a winner!")
                    if_winner = True
                    continue
                elif check_win(board=board, turn=current_turn) == 'draw':
                    print("It's a draw")
                    if_winner = True
                    continue
                change_player()
        continue_game = input("Play again? T/N ").lower()
        if continue_game != "t":
            cont = False


if __name__ == '__main__':
    main()
