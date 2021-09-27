fruits = ['apple', 'lemon', 'peach']

# listはiteratorではない
# next(fruits)

# print(iter(fruits))
# print()

fruits_iterator = iter(fruits)
next(fruits_iterator)