# exchanging apple and ideas
# If a gives apple to b and b gives apple to a.
# both have the same amount of apple.
# but if they share idea to each other than they both have 2 ideas.

class Human:
    apple = 0
    idea = 0

# mario has an apple and an idea
mario = Human()
mario.apple = 1
mario.idea = 1

# john has an apple and an idea
john = Human()
john.apple = 1
john.idea = 1

# exchanging apple between mario and john
def exchange_apple(you, me):
    temp = you.apple
    you.apple = me.apple
    me.apple = temp
    return you.apple, me.apple

# exchanging idea between mario and john
def exchange_idea(you,me):
    temp = you.idea
    you.idea += me.idea
    me.idea += temp
    return you.idea, me.idea

exchange_apple(mario, john)
print("Mario has {} apple and John has {} apple.".format(mario.apple, john.apple))

exchange_idea(mario, john)
print("Mario has {} ideas and John has {} ideas.".format(mario.idea, john.idea))
