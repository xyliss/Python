import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
# 读取演讲文本
with open("素材/dream.txt", "r", encoding="utf-8") as f:
    text = f.read()
# 读取停用词
stopwords = set()
with open("素材/stopwords.txt", "r", encoding="utf-8") as f:
    for line in f:
        stopwords.add(line.strip())
# 中文分词
words = jieba.lcut(text)
result = []
for word in words:
    if word not in stopwords and len(word) > 1:
        result.append(word)

text = " ".join(result)
# 读取背景图片
mask = np.array(Image.open("素材/background/heart.png"))
# 创建词云对象
wc = WordCloud(
    font_path="素材/font/SimHei.ttf",
    background_color="white",
    width=1000,
    height=700,
    mask=mask,
    max_words=200
)
# 生成词云
wc.generate(text)
# 保存词云
wc.to_file("dream_wordcloud.png")
# 显示词云
plt.imshow(wc)
plt.axis("off")
plt.show()