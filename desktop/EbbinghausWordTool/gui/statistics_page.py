import tkinter as tk
from database.database import Database_hy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


class StatisticsPage_hy:
    def __init__(self, parent):
        self.parent = parent
        self.db = Database_hy()
        self.words = self.db.load_words_hy()

        self.create_statistics_hy()

    def create_statistics_hy(self):
        total_words = len(self.words)
        mastered_words = sum(1 for word in self.words if word.mastered)
        unmastered_words = total_words - mastered_words
        total_reviews = sum(word.review_count for word in self.words)

        if total_words > 0:
            mastery_rate = (mastered_words / total_words) * 100
        else:
            mastery_rate = 0

        # 标题
        tk.Label(
            self.parent,
            text="学习数据统计",
            font=("微软雅黑", 20)
        ).pack(pady=20)

        # 数据显示
        tk.Label(
            self.parent,
            text=f"总单词数：{total_words}",
            font=("微软雅黑", 14)
        ).pack(pady=5)

        tk.Label(
            self.parent,
            text=f"已掌握：{mastered_words}",
            font=("微软雅黑", 14)
        ).pack(pady=5)

        tk.Label(
            self.parent,
            text=f"未掌握：{unmastered_words}",
            font=("微软雅黑", 14)
        ).pack(pady=5)

        tk.Label(
            self.parent,
            text=f"总复习次数：{total_reviews}",
            font=("微软雅黑", 14)
        ).pack(pady=5)

        tk.Label(
            self.parent,
            text=f"掌握率：{mastery_rate:.2f}%",
            font=("微软雅黑", 14)
        ).pack(pady=5)

        # 绘制图表
        self.draw_chart_hy(mastered_words, unmastered_words)

    def draw_chart_hy(self, mastered, unmastered):
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        categories = ["已掌握", "未掌握"]
        values = [mastered, unmastered]

        ax.bar(categories, values)
        ax.set_title("单词学习统计图")

        canvas = FigureCanvasTkAgg(fig, self.parent)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)