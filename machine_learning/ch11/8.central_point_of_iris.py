import numpy as np
from sklearn.datasets import load_iris

# 加载鸢尾花数据集
iris = load_iris()
X, y = iris.data, iris.target

# 获取不同标签类别的唯一值
unique_labels = np.unique(y)

# 初始化一个字典，用于存储不同类别的中心点
class_centers = {}

# 计算每个类别的中心点
for label in unique_labels:
    # 选择属于当前类别的样本
    class_samples = X[y == label]
    
    # 计算每个维度的均值，即中心点
    class_center = np.mean(class_samples, axis=0)
    
    # 将中心点存储到字典中
    class_centers[label] = class_center

# 打印不同类别的中心点
for label, center in class_centers.items():
    print(f"类别 {label} 的中心点： {center}")
