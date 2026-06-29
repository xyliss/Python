import csv

# 创建列表保存学生信息
student_list = []

# 打开成绩文件
with open("score.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    # 读取表头
    header = next(reader)
    header.append("总分")

    print("学生成绩信息：")
    print(header)

    # 读取每位同学成绩并计算总分
    for row in reader:
        total_score = sum(map(int, row[1:]))

        row.append(total_score)

        student_list.append(row)

        print(row)

# 按总分降序排序
student_list.sort(key=lambda x: x[-1], reverse=True)

print("\n按总分降序排序后的结果：")
for student in student_list:
    print(student)

# 写入新文件
with open("scoreSort.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(header)

    for student in student_list:
        writer.writerow(student)

print("\n排序后的成绩已成功保存到 scoreSort.csv 文件中！")