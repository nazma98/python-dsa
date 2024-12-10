new_dictionary = {"name": "Bondo", "age":3, "owner": "Shimul-san"}
print(new_dictionary)

# use dict() function to create dictionary
new_dictionary2 = dict(name = "Kopi", age=2, owner="Shishir")
print(new_dictionary2)

name = new_dictionary["name"]
print(name)

for value in new_dictionary.values():
    print(value)

for key, value in new_dictionary.items():
    print(key, value)

new_dictionary_copy = new_dictionary
print(new_dictionary_copy)
