'''
#构建一个m行，n列的矩阵，将其转置

import random
row_m = 3
col_n = 4

# 构造一个一个 3*4的矩阵
matrix = [[random.randint(0,9) for j in range(col_n)] for i in range(row_m)]
print(*matrix,sep= '\n')

# 构造一个4*3的空矩阵，矩阵中的每一个元素都是None
matrix_tans = [[None for j in range(row_m)] for i in range(col_n)]

# matrix_trans[i][j] = matrix[j][i]
for i in range(col_n):
    for j in range(row_m):
        matrix_tans[i][j] = matrix[j][i]

print(*matrix_tans,sep='\n')

# 构造一个m*n的矩阵，转置成n * m的矩阵

import random
row_m = 3
col_n = 4
# 构造一个 3 * 4的矩阵
# 不先开辟空间，用到的时候，append方法
matrix = [[random.randint(0,9) for j in range(col_n)] for i in range(row_m)]
print(*matrix,sep='\n')

matrix_trans = []

for i in range(col_n):
    row = []
    for j in range(row_m):
        row.append(matrix[j][i])
    matrix_trans.append(row)
print(*matrix_trans,sep='\n')


'''
# 构造一个m*n的矩阵，利用enumrate的方法转置
import random
row_m = 3
col_n = 4

matrix = [[random.randint(0,9) for j in range(col_n)] for i in range(row_m)]
print(*matrix,sep='\n')
matrix_trans = []
for i ,row in enumerate(matrix):
    for j ,col in enumerate(row):
        if i == 0:
            matrix_trans.append([])
        r = matrix_trans[j]
        r.append(col)

    matrix_trans.append(row)
print(*matrix_trans,sep='\n')










