import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix

# 导入鸢尾花数据集
iris = load_iris()
data = iris.data
feature_names = iris.feature_names

# 创建一个DataFrame
iris_df = pd.DataFrame(data, columns=feature_names)

# 添加目标（标签）列
iris_df['target'] = iris.target

# 创建散点图矩阵以可视化特征
scatter_matrix(iris_df, alpha=0.8, figsize=(12, 12), diagonal='hist')
plt.suptitle("Scatter Matrix of Iris Dataset Features", y=0.92)
plt.show()
