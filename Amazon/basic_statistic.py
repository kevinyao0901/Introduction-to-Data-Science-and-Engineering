import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 数据预处理
data = pd.read_csv('Amazon Customer Behavior Survey.csv')

# 2. 基本统计分析
statistics = data.describe()
print(statistics)

# 3. 探索性数据分析 (EDA)
# 例如，年龄与购买频率的关系
sns.scatterplot(x='age', y='Purchase_Frequency', data=data)
plt.title('Age vs Purchase Frequency')
plt.show()

# 4. 购物行为分析
# 比较购物篮完成频率
sns.countplot(x='Cart_Completion_Frequency', data=data)
plt.title('Cart Completion Frequency')
plt.show()

# 5. 评价和推荐系统分析
# 用户对评价可靠性的评分分布
sns.histplot(data['Review_Reliability'], bins=5, kde=True)
plt.title('Review Reliability Distribution')
plt.show()

# 6. 用户满意度和改进建议
# 用户满意度分布
sns.countplot(x='Shopping_Satisfaction', data=data)
plt.title('Shopping Satisfaction')
plt.show()

# 7. 建模和预测
# 可以使用 scikit-learn 或其他库进行建模和预测

# 8. 报告和可视化
# 汇总分析结果，创建报告或演示文稿
