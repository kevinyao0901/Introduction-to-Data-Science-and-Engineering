from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 导入鸢尾花数据集
iris = load_iris()
X = iris.data  # 特征矩阵
y = iris.target  # 目标向量

# 使用 train_test_split 切分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 输出训练集和测试集的大小
print("训练集样本数: ", len(X_train))
print("测试集样本数: ", len(X_test))
