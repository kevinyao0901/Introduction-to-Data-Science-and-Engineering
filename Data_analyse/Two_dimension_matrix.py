import numpy as np

# 定义二阶矩阵
matrix = np.array([[2, 1], [4, 5]])

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("特征值：", eigenvalues)
print("特征向量：\n", eigenvectors)
