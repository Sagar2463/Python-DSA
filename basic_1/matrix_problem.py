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

matrix3=[]

def matrix_Add (x,y):
    global matrix3
    # Check if matrices are the same size
    if len(x) != len(y) or len(x[0]) != len(y[0]):
      print("Matrices are not the same size")
    else:
        # Add corresponding elements together
        for i in range(len(x)):
            row = []
            for j in range(len(x[0])):
                row.append(x[i][j] + y[i][j])
            matrix3.append(row)  

matrix_Add(matrix1,matrix2)
print(matrix3)      


