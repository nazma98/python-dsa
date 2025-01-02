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
print(my_string.lower())

print(my_string.startswith('H'))
print(my_string.startswith('Hello'))

print(my_string.endswith('d'))
print(my_string.endswith('world!'))

print(my_string.find('o'))
print(my_string.find('w'))
print(my_string.find('llo'))

print(my_string.count('l'))

print(my_string.replace('world', 'universe'))

my_string = 'how are you doing'
my_list = my_string.split(" ")
print(my_list)
