import tkinter as tk
import json
import os


class SettingPage_hy:
    def __init__(self, parent):
        self.parent = parent

        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.config_path = os.path.join(base_dir, "data", "config.json")

        self.create_widgets_hy()

    def create_widgets_hy(self):
        tk.Label(
            self.parent,
            text="系统设置",
            font=("微软雅黑", 20)
        ).pack(pady=30)

        tk.Label(
            self.parent,
            text="每日任务数量：",
            font=("微软雅黑", 14)
        ).pack(pady=10)

        self.task_entry = tk.Entry(
            self.parent,
            font=("微软雅黑", 14),
            width=10
        )
        self.task_entry.pack(pady=10)

        current_count = self.load_config_hy()
        self.task_entry.insert(0, str(current_count))

        tk.Button(
            self.parent,
            text="保存设置",
            command=self.save_config_hy
        ).pack(pady=20)

    def load_config_hy(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                config = json.load(file)
                return config.get("daily_task_count", 20)
        except:
            return 20

    def save_config_hy(self):
        task_count = self.task_entry.get()

        config = {
            "daily_task_count": int(task_count)
        }

        with open(self.config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, ensure_ascii=False, indent=4)