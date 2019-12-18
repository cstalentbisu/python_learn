# 转置矩阵的方法
# # 原始矩阵：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # 方法一,i是行号，j是列号，注意j小于i表明是下三角
'''

matrix  = [[1,2,3],[4,5,6],[7,8,9]]
print(*matrix,sep='\n')

for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print('result')
print(*matrix,sep = '\n')
# 转置矩阵的方法
#  原始矩阵：matrix = [[1,2,3],[4,5,6],[7,8,9]]
#  方法二

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(*matrix,sep='\n')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i > j:
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print('result2')

print(*matrix,sep='\n')
# 转置矩阵的方法
#  原始矩阵：matrix = [[1,2,3],[4,5,6],[7,8,9]]
#  方法二

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(*matrix,sep='\n')
for i,row in enumerate(matrix):
    for j,col in enumerate(row):
        if i > j :
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

print('result3')

print(*matrix,sep='\n')
'''

# 构造一个n*n的方阵，进行转置
import random

n = 10

matrix = [[random.randint(0,100)for j in range(n)] for i in range(n)]
print(*matrix,sep='\n')

for i in range(n):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print('result4')
print(*matrix,sep='\n')
