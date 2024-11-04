# Given a list of numbers, find the sum and average of all numbers.
list = [12, 43, 54, 121, 32, 65, 78, 87]
sum =0
for i in list:
    sum = sum + i

print(f"Sum {sum}")
print(f"Average {sum / len(list)}")
# Write a program to find the maximum and minimum in a list without using max() or min().
max = list[0]
min = list[0]
for i in range(1, len(list)):
    if list[i] > max:
        max = list[i]

    if list[i]<min:
        min = list[i]

print(f"Maximum number is {max}")
print(f"Minimum number is {min}")
# Remove duplicates from a list of integers.