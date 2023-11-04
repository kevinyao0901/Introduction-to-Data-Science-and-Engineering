from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征矩阵
y = iris.target  # 目标向量

# 使用 train_test_split 切分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建KNN分类器
knn = KNeighborsClassifier(n_neighbors=3)  # 使用K=3

# 在训练集上训练分类器
knn.fit(X_train, y_train)

# 在训练集上进行预测
train_predictions = knn.predict(X_train)
train_accuracy = accuracy_score(y_train, train_predictions)
print("训练集准确性：", train_accuracy)

# 在测试集上进行预测
test_predictions = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)
print("测试集准确性：", test_accuracy)
