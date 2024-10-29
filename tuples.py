# Tuples
# Tuples are similar to list
# Except tuples are immutable
# Parentheses are used instead of square brackets

names = ("shimul", "nazma", "masuma", "shishir")
print(names[0])

print(names.index("shishir"))

# names[3] = "Shahana"
print(names)  # TypeError: 'tuple' object does not support item assignment

print(sorted(names)) # sorted() doesn't modify the original tuple


new_tuple = names + ("Shahana", "Monir")
print(new_tuple) # ('shimul', 'nazma', 'masuma', 'shishir', 'Shahana', 'Monir')

names += ("Shahana", "Monir")
print(names)
