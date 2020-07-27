class Person:
    apples = 0
    ideas = 0

johanna  = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 1
martin.ideas = 1

def exchange_apples(you, me):
    temp = you.apples
    you.apples = me.apples
    me.apples = temp

    return you.apples, me.apples

def exchange_ideas(you, me):
    temp = you.ideas
    you.ideas += me.ideas
    me.ideas += temp

    return you.ideas, me.ideas

print(exchange_apples(johanna, martin))

print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))

)print(exchange_ideas(johanna, martin))

print("Johanna has {} ideas and Martin has {} ideas.".format(johanna.ideas, martin.ideas))
