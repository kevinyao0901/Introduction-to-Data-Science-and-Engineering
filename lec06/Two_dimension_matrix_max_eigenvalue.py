import numpy as np

# 定义二阶矩阵
matrix = np.array([[2, 1], [4, 5]])

# 计算特征值
eigenvalues = np.linalg.eigvals(matrix)

# 获取最大特征值
max_eigenvalue = np.max(eigenvalues)

print("最大特征值：", max_eigenvalue)
