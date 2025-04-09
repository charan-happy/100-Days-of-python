# import random

# friends = ["charan", "cherry", "atm", "shika"]

# # 1 choice
# print(random.choice(friends))

# # 2 choice
# random_index=random.randint(0, len(friends))
# # random_index = random.randint(0, 4)

# print(friends[random_index])

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
print(dirty_dozen)


print(dirty_dozen[0]) #list 0 in dirty_dozen list i.e; fruits
print(dirty_dozen[1])


print(dirty_dozen[1][2])
print(dirty_dozen[1][3])