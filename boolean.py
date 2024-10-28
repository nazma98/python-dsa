# bool has two types of values
# True & False
# note: The values will be capitalized

done = True

if done:
    print("yes")
else:
    print("no")


# except number 0, all numbers are always True / truthy value
# using a value other than zero to see truthy value
done = 10
if done:
    print("it's not a zero!")
else:
    print("It's a zero!")

# using zero to see that zero is a falsy value
done_with_zero = 0
if done_with_zero:
    print("it's not a zero!")
else:
    print("It's a zero!")

# even negative values are truthy value

done_with_neg = -1
if done_with_neg:
    print("it's neg value!")
else:
    print("It's a zero!")


# empty strings are falsy value

name = ""

if name:
    print("String not empty!")
else:
    print("Empty string!")


#non-empty strings display truthy value

name = "Nazma"

if name:
    print(f"{name} is not empty!")
else:
    print(f"{name} is empty")
