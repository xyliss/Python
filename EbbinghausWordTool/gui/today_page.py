import tkinter as tk
from tkinter import messagebox
from database.database import Database_hy
from algorithms.ebbinghaus import Ebbinghaus_hy
import json
import os


class TodayPage_hy:
    def __init__(self, parent):
        self.parent = parent
        self.db = Database_hy()
        self.review = Ebbinghaus_hy()

        self.words = self.db.load_words_hy()
        self.current_index = 0
        self.show_meaning = False

        self.daily_task_count = self.load_config_hy()

        # 按设置限制任务数量
        self.words = self.words[:self.daily_task_count]

        self.create_widgets_hy()
        self.load_word_hy()

    def load_config_hy(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_dir, "data", "config.json")

        try:
            with open(config_path, "r", encoding="utf-8") as file:
                config = json.load(file)
                return config.get("daily_task_count", 20)
        except:
            return 20

    def create_widgets_hy(self):
        self.progress_label = tk.Label(
            self.parent,
            text="学习进度：0/0",
            font=("微软雅黑", 14)
        )
        self.progress_label.pack(pady=20)

        self.word_label = tk.Label(
            self.parent,
            text="",
            font=("微软雅黑", 30)
        )
        self.word_label.pack(pady=40)

        self.meaning_label = tk.Label(
            self.parent,
            text="",
            font=("微软雅黑", 20)
        )
        self.meaning_label.pack(pady=20)

        tk.Button(
            self.parent,
            text="显示释义",
            command=self.show_meaning_hy
        ).pack(pady=10)

        button_frame = tk.Frame(self.parent)
        button_frame.pack(pady=30)

        tk.Button(
            button_frame,
            text="认识",
            width=10,
            command=lambda: self.mark_word_hy("know")
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="模糊",
            width=10,
            command=lambda: self.mark_word_hy("vague")
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            button_frame,
            text="不会",
            width=10,
            command=lambda: self.mark_word_hy("forget")
        ).grid(row=0, column=2, padx=10)

    def load_word_hy(self):
        if not self.words:
            self.word_label.config(text="暂无单词")
            return

        if self.current_index >= len(self.words):
            self.word_label.config(text="今日任务完成")
            self.meaning_label.config(text="")
            self.progress_label.config(
                text=f"学习进度：{len(self.words)}/{len(self.words)}"
            )

            self.db.save_words_hy(self.words)

            messagebox.showinfo("完成", "今日学习完成！")
            return

        current_word = self.words[self.current_index]

        self.word_label.config(text=current_word.word)
        self.meaning_label.config(text="")

        self.progress_label.config(
            text=f"学习进度：{self.current_index + 1}/{len(self.words)}"
        )

    def show_meaning_hy(self):
        if self.words:
            current_word = self.words[self.current_index]
            self.meaning_label.config(text=current_word.meaning)

    def mark_word_hy(self, status):
        current_word = self.words[self.current_index]

        # 保存学习历史
        self.db.save_history_hy(current_word, status)

        updated_word = self.review.update_review_hy(current_word, status)

        self.words[self.current_index] = updated_word
        self.current_index += 1

        self.load_word_hy()