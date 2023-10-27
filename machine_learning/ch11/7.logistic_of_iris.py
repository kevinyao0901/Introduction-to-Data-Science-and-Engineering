import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建Logistic回归模型
model = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=10000)

# 在训练集上训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算分类准确度
accuracy = accuracy_score(y_test, y_pred)
print(f"分类准确度：{accuracy:.2f}")

# 打印分类报告
print("分类报告：")
print(classification_report(y_test, y_pred))

# 打印混淆矩阵
print("混淆矩阵：")
print(confusion_matrix(y_test, y_pred))
