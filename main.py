def check_winner(player1, player2):
    print(player1)
    print(player2)

    if player1 == "rock":
        if player2 == "rock":
            print("It's a draw")
        if player2 == "paper":
            print("Player 2 wins")
        if player2 == "scissors":
            print("Player 1 wins")

    if player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins")
        if player2 == "paper":
            print("It's a draw")
        if player2 == "scissors":
            print("Player 2 wins")

    if player1 == "scissors":
        if player2 == "rock":
            print("Player 2 wins")
        if player2 == "paper":
            print("Player 1 wins")
        if player2 == "scissors":
            print("It's a draw")

check_winner("rock", "scissors")