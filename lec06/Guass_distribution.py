import numpy as np
import matplotlib.pyplot as plt

# 生成100个服从正态分布的样本
samples = np.random.normal(loc=0, scale=1, size=100)

print(samples)

# 绘制直方图
plt.hist(samples, bins=20, density=True, alpha=0.7, color='skyblue')

# 添加标题和标签
plt.title('Histogram of Samples')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
