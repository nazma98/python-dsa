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


# append an item at the end of the list

foods.append("cake")
print(foods)


# extend is used to merge another list at the end of the existing list
foods.extend(["lemonade", False, 32])
print(foods)


# the += operator functions the same as extend method

foods += ["chicken", 11]
print(foods)

# remove an item from the list
foods.remove("pizza")
print(foods)

# use pop() method to remove and return the last item
print(foods.pop())
print(foods)

# insert an item in the middle of the list
foods.insert(3, "fish")
print(foods)

# insert multiple items using slice
foods[2:2] = ["raddish", "ramen", "kimchi"]
print(foods)

numbers = [21, 53, 14, 8, 45, 90]
# sort the numbers
numbers.sort()
print(numbers)

# reverse the sorted list
numbers.reverse()
print(numbers)
