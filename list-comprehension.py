# Create a list of the squares of numbers from 1 to 10.
list = []

for i in range(1,11):
    list.append(i*i)

print(list)

# Filter out squares that are greater than 50.
new_list = []
for i in list:
    if i> 50:
        new_list.append(i)

print(new_list)

# Create a new list of squares from the first list but add 1 to each value.
add_one_list = []

for i in list:
    add_one_list.append(i+1)

print(add_one_list)