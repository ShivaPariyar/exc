# creating a game

import random

print("choose:\n1.Rock \n2.Paper \n3.Scissor")
choose = int(input("Enter your choice"))

if choose == 1:
    print("your choice: Rock")
elif choose == 2:
    print("your choice: Paper")
else:
    print("your choice: Scissor")

computer = random.randint(1,3)
while True:
    if choose == computer:
        computer = random.randint(1, 3)
    break

if 1 == computer:
    print("Computer choice: Rock")
elif 2 == computer:
    print("Computer choice: Paper")
else:
    print("Computer choice: Scissor")

# condition to win
if choose == 1 and 2 == computer or computer == 1 and choose == 2:
    print("paper")
    win = "paper"

elif choose == 1 and 3 == computer or computer == 1 and choose == 3:
    print("Rock")
    win = "rock"
else:
    print("Scissor")
    win = "scissor"

if choose == win:
    print("you win")
else:
    print("computer win")














