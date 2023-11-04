from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

# 加载20newsgroups数据集
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# 获取文本数据和标签
text_data = newsgroups.data
labels = newsgroups.target

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 对文本数据进行向量化
tfidf_vectors = tfidf_vectorizer.fit_transform(text_data)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(tfidf_vectors, labels, test_size=0.2, random_state=42)

# 创建朴素贝叶斯分类器
naive_bayes_classifier = MultinomialNB()

# 在训练集上训练分类器
naive_bayes_classifier.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = naive_bayes_classifier.predict(X_test)

# 输出分类准确度
accuracy = metrics.accuracy_score(y_test, y_pred)
print("训练集和测试集的分类准确度:", accuracy)
