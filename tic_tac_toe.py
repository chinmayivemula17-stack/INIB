#Tic Tac Toe Game
while True:

    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]

    current_player = "X"


    def show_board():

        print()
        print(board[0], "|", board[1], "|", board[2])
        print("---------")

        print(board[3], "|", board[4], "|", board[5])
        print("---------")

        print(board[6], "|", board[7], "|", board[8])
        print()


    def check_winner():

        # Rows
        if board[0] == board[1] == board[2] != " ":
            return True

        if board[3] == board[4] == board[5] != " ":
            return True

        if board[6] == board[7] == board[8] != " ":
            return True

        # Columns
        if board[0] == board[3] == board[6] != " ":
            return True

        if board[1] == board[4] == board[7] != " ":
            return True

        if board[2] == board[5] == board[8] != " ":
            return True

        # Diagonals
        if board[0] == board[4] == board[8] != " ":
            return True

        if board[2] == board[4] == board[6] != " ":
            return True

        return False


    def check_tie():

        if " " not in board:
            return True

        return False


    while True:

        show_board()

        position = int(input(f"Player {current_player}, enter position (0-8): "))

        if board[position] == " ":

            board[position] = current_player

        else:
            print("Position already taken!")
            continue


        if check_winner():

            show_board()
            print(f"Player {current_player} wins!")
            break


        if check_tie():

            show_board()
            print("It's a tie!")
            break


        if current_player == "X":
            current_player = "O"

        else:
            current_player = "X"


    play_again = input("Do you want to play again? (yes/no): ")

    if play_again != "yes":
        print("Thanks for playing!")
        break
