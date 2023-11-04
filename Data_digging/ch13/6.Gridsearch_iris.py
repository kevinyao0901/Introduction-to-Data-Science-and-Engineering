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

# 输出最佳超参数和相应的准确性
best_k = grid_search.best_params_['n_neighbors']
best_accuracy = grid_search.best_score_
print("最佳超参数 k:", best_k)
print("最佳准确性:", best_accuracy)
