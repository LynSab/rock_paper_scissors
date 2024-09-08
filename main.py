def check_winner(player1, player2):
    print(f"Player 1 selection: {player1}")
    print(f"Player 2 selection: {player2}")

    outcomes = {
        "rock": {
            "rock": "draw",
            "paper": "loss",
            "scissors": "win"
        },
        "paper": {
            "rock": "win",
            "paper": "draw",
            "scissors": "loss"
        },
        "scissors": {
            "rock": "loss",
            "paper": "win",
            "scissors": "draw"
        }
    }

    if player1 not in outcomes or player2 not in outcomes:
        print("Invalid selection, please try again")
    else:
        player1_outcome = outcomes[player1][player2]

        if player1_outcome == "win":
            print("Player 1 Wins!")
        elif player1_outcome == "loss":
            print("Player 2 Wins!")
        else:
            print("Its a Draw!")