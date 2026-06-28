import tkinter as tk
from tkinter import ttk, simpledialog, filedialog, messagebox
from database.database import Database_hy
from models.word import Word_hy
from utils.importer import Importer_hy


class WordsPage_hy:
    def __init__(self, parent):
        self.parent = parent
        self.db = Database_hy()
        self.words = self.db.load_words_hy()

        self.create_widgets_hy()
        self.load_table_hy()

    def create_widgets_hy(self):
        # 标题
        tk.Label(
            self.parent,
            text="单词库管理",
            font=("微软雅黑", 20)
        ).pack(pady=20)

        # 表格
        columns = ("word", "meaning", "stage", "next_review")

        self.tree = ttk.Treeview(
            self.parent,
            columns=columns,
            show="headings"
        )

        self.tree.heading("word", text="单词")
        self.tree.heading("meaning", text="释义")
        self.tree.heading("stage", text="阶段")
        self.tree.heading("next_review", text="下次复习")

        self.tree.pack(expand=True, fill="both", padx=20, pady=20)

        # 按钮区域
        button_frame = tk.Frame(self.parent)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="添加单词",
            command=self.add_word_hy
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            button_frame,
            text="删除单词",
            command=self.delete_word_hy
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            button_frame,
            text="修改单词",
            command=self.edit_word_hy
        ).grid(row=0, column=2, padx=10)

        tk.Button(
            button_frame,
            text="导入TXT",
            command=self.import_txt_hy
        ).grid(row=0, column=3, padx=10)

        tk.Button(
            button_frame,
            text="导入CSV",
            command=self.import_csv_hy
        ).grid(row=0, column=4, padx=10)

    def load_table_hy(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.words = self.db.load_words_hy()

        for word in self.words:
            self.tree.insert(
                "",
                "end",
                values=(
                    word.word,
                    word.meaning,
                    word.stage,
                    word.next_review
                )
            )

    def add_word_hy(self):
        word_text = simpledialog.askstring("输入", "请输入单词：")
        meaning_text = simpledialog.askstring("输入", "请输入释义：")

        if word_text and meaning_text:
            new_word = Word_hy(word_text, meaning_text)
            result = self.db.add_word_hy(new_word)

            if result:
                self.load_table_hy()
                messagebox.showinfo("提示", "单词添加成功！")
            else:
                messagebox.showwarning("提示", "单词已存在，添加失败！")

    def delete_word_hy(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("提示", "请先选择要删除的单词！")
            return

        word_values = self.tree.item(selected_item)["values"]
        target_word = word_values[0]

        self.db.delete_word_hy(target_word)
        self.load_table_hy()

        messagebox.showinfo("提示", "单词删除成功！")

    def edit_word_hy(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("提示", "请先选择要修改的单词！")
            return

        word_values = self.tree.item(selected_item)["values"]
        old_word = word_values[0]

        new_word = simpledialog.askstring(
            "修改",
            "请输入新的单词：",
            initialvalue=word_values[0]
        )

        new_meaning = simpledialog.askstring(
            "修改",
            "请输入新的释义：",
            initialvalue=word_values[1]
        )

        if new_word and new_meaning:
            self.db.delete_word_hy(old_word)

            updated_word = Word_hy(new_word, new_meaning)
            self.db.add_word_hy(updated_word)

            self.load_table_hy()

            messagebox.showinfo("提示", "单词修改成功！")

    def import_txt_hy(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )

        if file_path:
            new_words = Importer_hy.import_txt_hy(file_path)

            count = 0

            for word in new_words:
                result = self.db.add_word_hy(word)
                if result:
                    count += 1

            self.load_table_hy()

            messagebox.showinfo(
                "提示",
                f"TXT导入成功！新增 {count} 个单词"
            )

    def import_csv_hy(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            new_words = Importer_hy.import_csv_hy(file_path)

            count = 0

            for word in new_words:
                result = self.db.add_word_hy(word)
                if result:
                    count += 1

            self.load_table_hy()

            messagebox.showinfo(
                "提示",
                f"CSV导入成功！新增 {count} 个单词"
            )