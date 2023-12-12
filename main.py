import random
player1 = input("Enter your choice. Choose one among - rock, paper, scissors.")
possibilities = ["rock", "paper", "scissors"]
player2= random.choice(possibilities)
print(f"\nPlayer1 chose {player1}, Player2 chose {player2}.\n")

if (player1 == player2):
    print("It's a tie!")
elif (player1 == "rock"):
    if (player2 == "scissors"):
        print("Player1 wins!")
    else:
        print("Player2 wins!")
elif (player1 == "paper"):
    if (player2 == "rock"):
        print("Player1 wins!")
    else:
        print("Player2 wins!")
elif (player1 == "scissors"):
    if (player2 == "paper"):
        print("Player1 wins!")
    else:
        print("Player2 wins!")