import random

hand = input("What would you like to test (rock, paper, scissor): ").lower()

i = 0
numWins = 0
while i < 100:
    def computer():
        number = random.randint(0, 3)
        if number == 0:
            return "rock"
        elif number == 1:
            return "paper"
        elif number == 2:
            return "scissor"
    if (hand == "rock" and computer() == "scissor") or (hand == "paper" and computer() == "rock") or (hand == "scissor" and computer() == "paper"):
        numWins += 1
    i += 1

print("Percent Wins Playing " + hand + ": " + str(numWins/100.0))
