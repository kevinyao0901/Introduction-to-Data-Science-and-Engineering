import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import LeaveOneOut, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征矩阵
y = iris.target  # 目标向量

# 创建KNN分类器
knn = KNeighborsClassifier()

# 定义超参数k的搜索范围
param_grid = {'n_neighbors': [1, 3, 5, 8, 10, 12, 15, 20, 50, 100]}

# 创建 LeaveOneOut 交叉验证迭代器
loo = LeaveOneOut()

# 创建GridSearchCV对象，使用五折交叉验证
grid_search = GridSearchCV(knn, param_grid, cv=loo, scoring='accuracy')

# 执行网格搜索
grid_search.fit(X, y)

# 获取超参数和对应的准确性
k_values = param_grid['n_neighbors']
accuracies = grid_search.cv_results_['mean_test_score']

# 可视化准确性随k值的变化
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, marker='o', linestyle='-')
plt.title("Accuracy vs. Number of Neighborsk (KNN)")
plt.xlabel("hyperparameter_k")
plt.ylabel("Five-Fold Cross-Validation")
plt.grid(True)

# 找到最佳超参数k
best_k = grid_search.best_params_['n_neighbors']
best_accuracy = grid_search.best_score_

# 在图上标注最佳超参数
plt.annotate(f'Best k={best_k}\nBest Accuracy={best_accuracy:.3f}',
             xy=(best_k, best_accuracy),
             xytext=(best_k + 10, best_accuracy - 0.05),
             arrowprops={'arrowstyle': '->'})

plt.show()
