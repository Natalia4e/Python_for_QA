#Напишите функцию для транспонирования матрицы

matrix = [[1,2,3], [3,4,2]]
print(matrix)

def transp_matrix(matrix_):
    raws = len(matrix_)
    column = len(matrix_[0])
    tr_matrix = [[None]* raws for _ in range (column)]
    for i in range(raws):
        for j in range(column):
            tr_matrix[j][i] = matrix_[i][j]
    return tr_matrix

print(transp_matrix(matrix))



