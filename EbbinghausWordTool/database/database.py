import json
import os
from datetime import datetime
from models.word import Word_hy


class Database_hy:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(base_dir, "data", "words.json")
        self.history_path = os.path.join(base_dir, "data", "history.json")

    # 读取单词数据
    def load_words_hy(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Word_hy.from_dict_hy(item) for item in data]
        except FileNotFoundError:
            return []

    # 保存单词数据
    def save_words_hy(self, words):
        data = [word.to_dict_hy() for word in words]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # 添加单词（带查重）
    def add_word_hy(self, new_word):
        words = self.load_words_hy()

        for word in words:
            if word.word == new_word.word:
                return False

        words.append(new_word)
        self.save_words_hy(words)

        return True

    # 删除单词
    def delete_word_hy(self, target_word):
        words = self.load_words_hy()
        words = [word for word in words if word.word != target_word]
        self.save_words_hy(words)

    # 保存学习历史记录
    def save_history_hy(self, word, status):
        try:
            with open(self.history_path, "r", encoding="utf-8") as file:
                history = json.load(file)
        except:
            history = []

        record = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "word": word.word,
            "status": status
        }

        history.append(record)

        with open(self.history_path, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)