items = ["pen", "paper", "pencil", "sharpner", "eraser"]

items.sort()
print(items) # ['eraser', 'paper', 'pen', 'pencil', 'sharpner']

new_items = ["Book", "Khata", "Pen", "pencil", "box"]
new_items.sort()
print(new_items) # ['Book', 'Khata', 'Pen', 'box', 'pencil']

new_items_copy = new_items
print(new_items_copy)

# to not care about uppercase and lowercase letter
new_items.sort(key=str.lower)
print(new_items) # ['Book', 'box', 'Khata', 'Pen', 'pencil']


# instead of modifying the original list
print(sorted(new_items, key=str.lower))

mixed_items = [12, "food", "water", True]
mixed_items.sort()
print(mixed_items) # TypeError: '<' not supported between instances of 'str' and 'int'
