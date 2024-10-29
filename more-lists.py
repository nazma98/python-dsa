# lists contain different types of values

foods = ["rice", 23, "pasta", "pizza", True]

# check if an item is in the list
print("pizza" in foods) # True


print("noodles" in foods) # False

# indexing starts with 0
print(foods[3]) # pizza

# update an item in the list
foods[1] = "noodles"

print(foods)


# negative indexing means starting from the end of the list
print(foods[-2]) # pizza


# slice the list items
print(foods[2:4]) # ['pasta', 'pizza']

# length of list
print(len(foods))
