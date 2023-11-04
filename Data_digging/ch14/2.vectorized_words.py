from sklearn.feature_extraction.text import CountVectorizer

# 文本数据
text = [
    "House Baratheon - Descended from Orys Baratheon they are Lords of The Stormlands, Kings on the Iron Throne and Lords of Dragonstone. The head of house at the start of the novels is King Robert Baratheon, however Lord Stannis Baratheon holds Dragonstone, and Lord Renly Baratheon holds Storm's End and the Stormlands. The sigil of House Baratheon is a crowned black stag on a cloth of gold. Their house words are Ours is the Fury",

"House Lannister - Lords of Casterly Rock and ruling house of The Westerlands. Traditionally the current Lord is Warden of the West. At the start of the novels House Lannister is lead by Lord Tywin Lannister. The sigil of House Lannister is a golden lion on a cloth of red. Their house words are Hear Me Roar.",

"House Stark - Lords of Winterfell and ruling house of The North. The current Lord is traditionally Warden of the North. At the start of the novels House Stark is led by Lord Eddard Stark. Their sigil is grey direwolf on a cloth of white. Their house words are Winter is Coming",

"House Arryn - Lords of the Eyrie and ruling house of the Vale of Arryn. The current Lord is traditionally Warden of the East. At the start of the novels House Arryn is lead by Robert Arryn. Their sigil is a sky blue falcon over a white moon on a cloth of sky blue. Their house words are As High as Honor.",

"House Tyrell - Lords of Highgarden and ruling house of The Reach. The current Lord is traditionally Warden of the South. At the start of the novels House Tyrell is lead by Lord Mace Tyrell. Their sigil is a golden rose on a cloth of green. Their house words are Growing Strong.",

"House Greyjoy - Lords of Pyke and ruling house of The Iron Islands. At the start of the novels House Greyjoy is lead by Lord Balon Greyjoy. Their sigil is a golden kraken on a black cloth. Their house words are We Do Not Sow.",

"House Tully - Lords of Riverrun and ruling house of The Riverlands. At the start of the novels House Tully is lead by Lord Hoster Tully. Their sigil is a silver trout leaping out of the water on a purple cloth. Their house words are Family, Duty, Honor.",

"House Martell - Lords of Sunspear, The Water Gardens and the ruling house of the Dorne. At the start of the novels House Martell are lead by Prince Doran Martell. Their sigil is an orange sun pierced with a spear on a yellow cloth. Their house words are Unbowed, Unbent, Unbroken."
]

# 创建词袋模型
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text)

# 输出词袋模型的结果向量
print("词袋模型的结果向量:")
print(X.toarray())
