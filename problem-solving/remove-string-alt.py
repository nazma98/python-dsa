def remove_string(strings, min_length):
    result = []
    for s in strings:
        if len(s) >= min_length:
            result.append(s)
    return result

fruits = ['banana', 'grape', 'kiwi', 'jackfruit', 'berry', 'blackberry', 'mango']
print(remove_string(fruits, 6))