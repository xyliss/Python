# Ebbinghaus Word Tool

## 项目简介

Ebbinghaus Word Tool（艾宾浩斯背单词工具）是一款基于 Python 开发的桌面单词学习工具，结合艾宾浩斯遗忘曲线算法实现智能复习计划，帮助用户科学记忆单词，提高学习效率。

本项目采用 Tkinter 构建图形界面，支持单词管理、批量导入、学习统计以及本地数据存储。

---

## 功能特点

- 单词管理（增删改查）
- 支持 TXT / CSV 批量导入
- 艾宾浩斯遗忘曲线智能复习
- 单词掌握状态记录（认识 / 模糊 / 不会）
- 学习进度展示
- 学习数据统计
- 图表可视化分析
- 每日任务数量设置
- 本地 JSON 数据存储

---

## 技术栈

- Python
- Tkinter
- JSON
- Matplotlib
- CSV
- Datetime

---

## 项目结构

```text
EbbinghausWordTool
│
├── main.py
│
├── models
│   └── word.py
│
├── database
│   └── database.py
│
├── algorithms
│   └── ebbinghaus.py
│
├── gui
│   ├── main_window.py
│   ├── today_page.py
│   ├── words_page.py
│   ├── statistics_page.py
│   └── setting_page.py
│
├── utils
│   └── importer.py
│
├── data
│   ├── words.json
│   ├── history.json
│   └── config.json