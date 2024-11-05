# Create a nested list representing a 3x3 matrix.
matrix = []
for i in range(3):
    row = []
    for j in range(3):
        num = int(input())
        row.append(num)
    matrix.append(row)


print(matrix)
                      
# Access the element in the second row, third column.
# Update the element in the first row, second column to a new value.
# Print the matrix as a formatted grid.