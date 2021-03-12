def matrix_transpose(matrix):
    matrix_t = []
    m = len(matrix)
    n = len(matrix[0])
    for x in range(0, n):
        row = []
        for y in range(0, m):
            row.append(matrix[y][x])
        matrix_t.append(row)
    return matrix_t
mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))
