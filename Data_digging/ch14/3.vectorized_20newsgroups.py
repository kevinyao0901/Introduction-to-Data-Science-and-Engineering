from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

# 加载20newsgroups数据集
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# 获取文本数据
text_data = newsgroups.data

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer()

# 对文本数据进行向量化
tfidf_vectors = tfidf_vectorizer.fit_transform(text_data)

# 输出第一个文本的结果向量
print("第一个文本的TF-IDF结果向量:")
print(tfidf_vectors[0].toarray())
