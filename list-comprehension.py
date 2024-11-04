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