from sklearn.datasets import load_iris
from sklearn.model_selection import LeaveOneOut
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征矩阵
y = iris.target  # 目标向量

# 创建KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)  # 使用K=3

# 创建 LeaveOneOut 交叉验证迭代器
loo = LeaveOneOut()

# 初始化变量以存储准确性
accuracies = []

# 执行留一验证
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # 在训练集上训练分类器
    knn.fit(X_train, y_train)

    # 在测试集上进行预测
    test_predictions = knn.predict(X_test)

    # 计算准确性并存储
    accuracy = accuracy_score(y_test, test_predictions)
    accuracies.append(accuracy)

# 计算平均准确性
average_accuracy = sum(accuracies) / len(accuracies)
print("平均准确性：", average_accuracy)
