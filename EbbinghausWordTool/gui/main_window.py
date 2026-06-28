import tkinter as tk
from gui.today_page import TodayPage_hy
from gui.words_page import WordsPage_hy
from gui.statistics_page import StatisticsPage_hy
from gui.setting_page import SettingPage_hy


class MainWindow_hy:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("艾宾浩斯背单词工具")
        self.root.geometry("900x600")

        self.create_layout_hy()

    def create_layout_hy(self):
        # 左侧导航栏
        self.left_frame = tk.Frame(self.root, width=200, bg="#dcdcdc")
        self.left_frame.pack(side="left", fill="y")

        # 右侧内容区
        self.right_frame = tk.Frame(self.root, bg="white")
        self.right_frame.pack(side="right", expand=True, fill="both")

        # 按钮
        tk.Button(self.left_frame, text="今日任务",
                  command=self.show_today_hy).pack(fill="x", pady=10)

        tk.Button(self.left_frame, text="单词库",
                  command=self.show_words_hy).pack(fill="x", pady=10)

        tk.Button(self.left_frame, text="数据统计",
                  command=self.show_statistics_hy).pack(fill="x", pady=10)

        tk.Button(self.left_frame, text="设置",
                  command=self.show_setting_hy).pack(fill="x", pady=10)

        self.show_today_hy()

    def clear_right_hy(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def show_today_hy(self):
        self.clear_right_hy()
        TodayPage_hy(self.right_frame)

    def show_words_hy(self):
        self.clear_right_hy()
        WordsPage_hy(self.right_frame)

    def show_statistics_hy(self):
        self.clear_right_hy()
        StatisticsPage_hy(self.right_frame)

    def show_setting_hy(self):
        self.clear_right_hy()
        SettingPage_hy(self.right_frame)

    def run_hy(self):
        self.root.mainloop()