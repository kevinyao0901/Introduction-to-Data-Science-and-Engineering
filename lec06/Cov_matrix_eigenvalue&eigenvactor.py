import numpy as np

# 定义三阶矩阵
matrix = np.array([[1, -1, 4], [2, 1, 3], [1, 3, -1]])

# 计算协方差矩阵
cov_matrix = np.cov(matrix.T)

# 定义迭代次数和初始向量
iterations = 1000
v = np.array([1, 1, 1])

# 进行幂迭代计算
for i in range(iterations):
    w = np.dot(cov_matrix, v)
    v = w / np.linalg.norm(w)

# 计算特征值和特征向量
eigenvalues = []
eigenvectors = []
for i in range(cov_matrix.shape[0]):
    vi = v[i]
    ei = np.dot(np.dot(cov_matrix, vi), vi) / np.dot(vi, vi)
    eigenvalues.append(ei)
    eigenvectors.append(vi)

# 打印结果
print("特征值和对应的特征向量：")
for i in range(cov_matrix.shape[0]):
    print(f"特征值 {i+1}: {eigenvalues[i]}")
    print(f"特征向量 {i+1}: {eigenvectors[i]}")
    print()
