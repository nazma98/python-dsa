try:
    result = 10 / 0
    value = int(input("Enter a number: "))
    print(value)

except ZeroDivisionError as err:
    print(err)

except ValueError as err:
    print(err)