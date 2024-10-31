# Given a list of strings, remove all the strings that have a length less than a given value: 
# a. ["apple", "banana", "grape", "kiwi"]. Example: length 6 (Resulting list is ["banana"])

def filter_string(strings, min_length):
    strings_copy = strings.copy()

    for s in strings_copy:
        if len(s) < min_length:
            strings.remove(s)
            print(strings)

    return strings

fruits = ["apple", "banana", "grape", "kiwi", "jackfruit", "berry", "blackberry", "mango"]
length = 6

print(filter_string(fruits, 6))
