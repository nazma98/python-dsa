my_string = "Hello world!"
print(my_string)

another_string = 'I\'m a programmer'
print(another_string)

char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

substring2 = my_string[::2]
print(substring2)

reversed_string = my_string[::-1]
print(reversed_string)

if 'e' in my_string:
    print('true')
else:
    print('false')

if 'ello' in my_string:
    print('true')
else:
    print('false')

new_string = '   Nazma Sarker  '
print(new_string)

new_string = new_string.strip()
print(new_string)

print(my_string.upper())
