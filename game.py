def is_win(game):
    win = False
    # rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win


def main():
    # Initialize the game board
    game = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Player 1 (X) starts

    print("X = Player 1")
    print("O = Player 2")

    won = False
    for n in range(9):
        player_num = '1' if current_player == 'X' else '2'
        print(f"Player {player_num}: ", end="")

        while True:
            try:
                print("Which cell to mark? i:[1..3], j:[1..3]: ", end="")
                i, j = map(int, input().split())
            except ValueError:
                print("Invalid input! Please enter two integers.")
                continue

            i, j = i - 1, j - 1  # convert to 0-based indices
            if not (0 <= i <= 2 and 0 <= j <= 2):
                print("Invalid range! Please enter values 1-3.")
                continue
            if game[i][j] != ' ':
                print("Cell already occupied! Choose another.")
                continue
            break

        game[i][j] = current_player

        if is_win(game):
            print("Win!")
            won = True
            break

        current_player = 'O' if current_player == 'X' else 'X'

    if not won:  # no winner after all 9 cells filled
        print("Tie!")

    # Show the game to console
    print(game[0][0] + " " + game[0][1] + " " + game[0][2])
    print(game[1][0] + " " + game[1][1] + " " + game[1][2])
    print(game[2][0] + " " + game[2][1] + " " + game[2][2])


if __name__ == "__main__":
    main()
