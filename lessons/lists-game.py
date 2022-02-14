"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
rolls.append(randint(1, 6))
print(rolls) 

# access an individual item 
print(rolls[0])
print(rolls[1]) 

# access the length of the list 
print(len(rolls))

# access the list item of the list
print(rolls[len(rolls) - 1])