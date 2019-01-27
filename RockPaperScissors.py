import random

cont = "yes"

while cont == "yes":
    hand = input("rock, paper, scissor: ").lower()

    while hand != "rock" and hand != "paper" and hand != "scissor":
        hand = input("rock, paper, scissor: ").lower()

    def computer():
        number = random.randint(0, 3)
        if number == 0:
            return "rock"
        elif number == 1:
            return "paper"
        elif number == 2:
            return "scissor"

    numWins = 0
    if hand == computer():
        print("You tied")
    elif (hand == "rock" and computer() == "scissor") or (hand == "paper" and computer() == "rock") or (hand == "scissor" and computer() == "paper"):
        print("You won")
        numWins += 1
    else:
        print("You lost")

    print("Number of Wins: " + str(numWins))

    cont = input("Do you want to play again? ").lower()
