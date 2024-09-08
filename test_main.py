import main

# player 1 selection rock
def test_rock_draw(capsys):
    main.check_winner("rock", "rock")
    captured = capsys.readouterr()
    assert "Its a Draw!\n" in captured.out

def test_rock_vs_paper(capsys):
    main.check_winner("rock", "paper")
    captured = capsys.readouterr()
    assert "Player 2 Wins!\n" in captured.out

def test_rock_vs_scissors(capsys):
    main.check_winner("rock", "scissors")
    captured = capsys.readouterr()
    assert "Player 1 Wins!\n" in captured.out

# player 1 selection paper
def test_paper_draw(capsys):
    main.check_winner("paper", "paper")
    captured = capsys.readouterr()
    assert "Its a Draw!\n" in captured.out

def test_paper_vs_rock(capsys):
    main.check_winner("paper", "rock")
    captured = capsys.readouterr()
    assert "Player 1 Wins!\n" in captured.out

def test_paper_vs_scissors(capsys):
    main.check_winner("paper", "scissors")
    captured = capsys.readouterr()
    assert "Player 2 Wins!\n" in captured.out

# player 1 selection scissors
def test_scissors_draw(capsys):
    main.check_winner("scissors", "scissors")
    captured = capsys.readouterr()
    assert "Its a Draw!\n" in captured.out

def test_scissors_vs_rock(capsys):
    main.check_winner("scissors", "rock")
    captured = capsys.readouterr()
    assert "Player 2 Wins!\n" in captured.out

def test_scissors_vs_paper(capsys):
    main.check_winner("scissors", "paper")
    captured = capsys.readouterr()
    assert "Player 1 Wins!\n" in captured.out

# invalid selection
def test_player1_invalid(capsys):
    main.check_winner("puppy", "paper")
    captured = capsys.readouterr()
    assert "Invalid selection, please try again\n" in captured.out

def test_player2_invalid(capsys):
    main.check_winner("rock", "pepperoni")
    captured = capsys.readouterr()
    assert "Invalid selection, please try again\n" in captured.out

def test_both_invalid(capsys):
    main.check_winner("aliens", "sauce")
    captured = capsys.readouterr()
    assert "Invalid selection, please try again\n" in captured.out