def add_matrices2D(mat1, mat2):
    result = []
    if (len(mat1) == len(mat2)) and (len(mat1[0]) == len(mat2[0])):
        for x in range(len(mat1)):
            row = []
            for y in range(len(mat1[0])):
                row.append(mat1[x][y] + mat2[x][y])
            result.append(row)
        return result
    return None

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))
