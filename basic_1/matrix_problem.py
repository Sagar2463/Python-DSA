# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize an empty result matrix outside the loops
matrix3 = []

# Outer loop: Iterate through each row
for i in range(len(matrix1)):  # i is the row index
    trow = []  # Initialize a temporary row for the result
    for j in range(len(matrix1[0])):  # j is the column index
        # Perform element-wise addition
        trow.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(trow)  # Append the completed row to matrix3

# Print the resulting matrix
for row in matrix3:
    print(row)
