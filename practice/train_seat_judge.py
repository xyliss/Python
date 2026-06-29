# Python高铁座位判断程序（字符串应用）
# 1. 获取用户输入的座位号
seat_num = input("请输入高铁座位号（如3A、17F）：")

# 2. 初始化变量，分离数字（排数）和字母（座位）
row_str = ""  # 存储排数字符串
seat_char = ""  # 存储座位字母
is_legal = True  # 合法性标记

# 遍历字符串，拆分数字和字母
for char in seat_num:
    if char.isdigit():
        row_str += char
    else:
        seat_char += char

# 3. 校验排数是否合法（1-17）
if not row_str or not seat_char:
    is_legal = False
else:
    row = int(row_str)
    if row < 1 or row > 17:
        is_legal = False

# 4. 校验座位字母是否合法（转大写，排除E）
seat_char = seat_char.upper()
legal_chars = ["A", "B", "C", "D", "F"]
if seat_char not in legal_chars:
    is_legal = False

# 5. 判断座位位置并输出结果
if is_legal:
    if seat_char == "A" or seat_char == "F":
        print("窗口")
    elif seat_char == "C" or seat_char == "D":
        print("过道")
    elif seat_char == "B":
        print("中间座席")
else:
    print("输入错误")