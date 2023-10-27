import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data

# 创建K-means模型并指定簇的数量（这里假设为3，因为鸢尾花数据集有3个类别）
kmeans = KMeans(n_clusters=3, random_state=0)

# 使用K-means模型进行聚类
kmeans.fit(X)

# 获取聚类结果（每个样本所属的簇）
labels = kmeans.labels_

# 获取聚类的中心点
centers = kmeans.cluster_centers_

# 可视化聚类结果
plt.figure(figsize=(8, 6))

for i in range(3):
    cluster_points = X[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i + 1}')

plt.scatter(centers[:, 0], centers[:, 1,], c='black', s=200, marker='X', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('K-means Clustering of Iris Data')
plt.show()
