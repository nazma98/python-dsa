employee_file = open("employee.txt", "r")

# check if the file is readable
print(employee_file.readable())

# read the entire file
# print(employee_file.read())

# read the first line
# print(employee_file.readline())

# read the first two lines
# print(employee_file.readline())
# print(employee_file.readline())

# reads all the lines in a list
# print(employee_file.readlines())

# read from a specific index 
# print(employee_file.readlines()[2])

# for loop 
for employee in employee_file.readlines():
    print(employee)


# close the file
employee_file.close()