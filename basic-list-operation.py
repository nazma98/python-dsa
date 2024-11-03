# fav_fruits = ["Apple", "Mango", "Banana", "Grape", "Strawberry"]

# print(fav_fruits)

new_list = []
for i in range(5):
    new_list.append(input("Enter your fav fruit: "))

print(new_list)

# Add new fruit
new_list.append(input("Enter a new fav fruit: "))
print(new_list)

# remove a fruit from the list
new_list.remove(input("Enter the fruit you want to remove: "))

print(new_list)

# Sort the list in alphabetical order
new_list.sort()
print(f"The sorted list {new_list}")

reversed_list = new_list[::-1]
print(f"The reversed list is here {reversed_list}")

# print first and last item of the list
print(f"The first item is {new_list[0]} and the last item is {new_list[-1]}")