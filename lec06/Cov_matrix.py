import numpy as np

# 定义三阶矩阵
matrix = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

# 计算协方差矩阵
covariance_matrix = np.cov(matrix)

print("协方差矩阵：")
print(covariance_matrix)


