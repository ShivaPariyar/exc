import random

choose = random.randint(1,3)
print(choose)

computer = random.randint(1,3)


while True:
    if choose == computer:
        computer = random.randint(1, 3)
    break

print(computer)