# List Slicing

#     Create a list of the first 20 natural numbers.
natural_num = list(range(1,21))
print(natural_num)

#     Extract a sublist of the first 5 elements.
print(natural_num[:5])


#     Extract the last 5 elements of the list.
print(natural_num[15:20])
print(natural_num[15:])
print(natural_num[-5:])

#     Extract every other element from the list.

print(natural_num[::2]) # odd
print(natural_num[1::2]) # even
#     Reverse the list using slicing.