import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

player = False

comp_score = 0

players_score = 0

while True:

    player = input("Rock, Paper or Scissors? ").capitalize()

    ### conditions

    if player == computer:

        print("Amazing !!!, A Tie.")
    
    elif player == "Rock":

        if computer == "Paper":

            print("You lose !", computer, "covers", player)

            comp_score += 1

        else:

            print("Amazing !!! You Win !", player, "smashes", computer)

            players_score += 1

    elif player == "Paper":

        if computer == "Scissors":

            print("You Lose...", computer, "cut", player)

            comp_score += 1

        else:

            print("Amazing !!! You Win", player, "covers", computer)

            players_score += 1

    elif player == "Scissors":

        if computer == "Rock":

            print("You Lose...", computer, "smashes", player)

            comp_score += 1

        else:

            print("Amazing !!! You Win", player, "cut", computer)

            players_score += 1

    elif player == "End":

        print("Final Scores : ")
        print(f"CPU:{cpu_score}")
        print(f"player:{players_score}")

        break